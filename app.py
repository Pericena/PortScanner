from flask import Flask, render_template, request
import nmap
import yaml
import openai
from datetime import datetime

# Crear la aplicación Flask
app = Flask(__name__)

# Cargar configuración desde un archivo YAML
def load_config():
    try:
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)
        print("[INFO] Configuración cargada correctamente.")
        return config
    except FileNotFoundError:
        print("[ERROR] El archivo 'config.yaml' no existe. Asegúrate de crearlo con las configuraciones necesarias.")
    except Exception as e:
        print(f"[ERROR] Error al cargar el archivo de configuración: {e}")
    return {}

# Cargar la configuración
config = load_config()

# Configurar la clave de la API de OpenAI
if 'OPENAI_API_KEY' in config:
    openai.api_key = config['OPENAI_API_KEY']
    print("[INFO] OpenAI API configurado correctamente.")
else:
    print("[WARNING] La clave API de OpenAI no está configurada.")

# Ruta principal
@app.route('/')
def home():
    print("[INFO] Acceso a la página principal.")
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form.get('target')
    scan_type = request.form.get('scan_type')  # <- Nuevo parámetro

    if not target:
        print("[ERROR] No se ingresó un objetivo para escanear.")
        return render_template('index.html', error="Por favor, ingresa un objetivo válido.")

    print(f"[INFO] Iniciando escaneo para el objetivo: {target} con tipo: {scan_type}")
    nm = nmap.PortScanner()

    # Configurar argumentos según tipo de escaneo
    scan_arguments = "-sS -sV -O -A"  
    if scan_type == "fast":
        scan_arguments = "-F"
    elif scan_type == "tcp_syn":
        scan_arguments = "-sS"
    elif scan_type == "service_detection":
        scan_arguments = "-sV"
    elif scan_type == "os_detection":
        scan_arguments = "-O"
    elif scan_type == "udp":
        scan_arguments = "-sU"

    try:
        results = nm.scan(hosts=target, arguments=scan_arguments)
        print(f"[INFO] Resultados del escaneo: {results}")

        open_ports = []
        tcp_results = results['scan'].get(target, {}).get('tcp', {})
        for port, info in tcp_results.items():
            if info['state'] == 'open':
                open_ports.append({
                    'port': port,
                    'name': info.get('name', 'N/A'),
                    'product': info.get('product', 'N/A'),
                    'version': info.get('version', 'N/A'),
                    'extrainfo': info.get('extrainfo', 'N/A')
                })
        print(f"[INFO] Puertos abiertos detectados: {open_ports}")
        return render_template('results.html', target=target, open_ports=open_ports, scan_type=scan_type)
    
    except KeyError as ke:
        print(f"[ERROR] El escaneo no encontró datos para el objetivo. Error: {ke}")
        return render_template('index.html', error="No se encontraron datos para el objetivo ingresado.")
    except Exception as e:
        print(f"[ERROR] Error al escanear: {e}")
        return render_template('index.html', error=f"Error al escanear: {str(e)}")


@app.route('/action', methods=['POST'])
def action():
    port = request.form.get('port')
    product = request.form.get('product')
    version = request.form.get('version')
    extra_info = request.form.get('extrainfo')

    print(f"[INFO] Acción recibida para el puerto {port} con producto {product}, versión {version}, extra: {extra_info}")

    advice = "La funcionalidad de generación de información no está disponible en este momento."
    risk_level = "Desconocido"

    if openai.api_key:
        try:
            solicitud = (
                f"Actúa como un analista de ciberseguridad. Analiza el puerto {port} detectando "
                f"riesgos, vulnerabilidades, amenazas conocidas del producto {product} "
                f"(versión {version}), y sugiere medidas de mitigación. "
                f"Información adicional: {extra_info}. Resume también el nivel de riesgo (Alto, Medio, Bajo)."
            )

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un experto en análisis de seguridad de redes."},
                    {"role": "user", "content": solicitud}
                ],
                temperature=0.3,
                max_tokens=500
            )
            full_response = response['choices'][0]['message']['content'].strip()
            advice = full_response
            if "alto" in full_response.lower():
                risk_level = "Alto"
            elif "medio" in full_response.lower():
                risk_level = "Medio"
            elif "bajo" in full_response.lower():
                risk_level = "Bajo"

        except Exception as e:
            print(f"[ERROR] Error al obtener respuesta de OpenAI: {e}")
            advice = "Hubo un error al intentar obtener la información de OpenAI."

    return render_template('action.html', port=port, advice=advice, product=product, version=version, extra_info=extra_info, risk_level=risk_level)

if __name__ == '__main__':
    print("[INFO] Aplicación iniciada en modo depuración.")
    app.run(debug=True, host='0.0.0.0', port=5200)
