from flask import Flask, render_template, request
import nmap
import yaml
import openai

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

config = load_config()

# Inicializar OpenAI si se encuentra en la configuración
if 'openai_api_key' in config:
    openai.api_key = config['openai_api_key']
    print("[INFO] OpenAI API configurado correctamente.")
else:
    print("[WARNING] La clave API de OpenAI no está configurada.")

@app.route('/')
def home():
    print("[INFO] Acceso a la página principal.")
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    target = request.form.get('target')
    if not target:
        print("[ERROR] No se ingresó un objetivo para escanear.")
        return render_template('index.html', error="Por favor, ingresa un objetivo válido.")

    print(f"[INFO] Iniciando escaneo para el objetivo: {target}")
    nm = nmap.PortScanner()

    try:
        results = nm.scan(hosts=target, arguments='-sS -sV -O -A')
        print(f"[INFO] Resultados del escaneo: {results}")

        open_ports = []
        for port, info in results['scan'][target]['tcp'].items():
            if info['state'] == 'open':
                open_ports.append({
                    'port': port,
                    'name': info.get('name', 'N/A'),
                    'product': info.get('product', 'N/A'),
                    'version': info.get('version', 'N/A'),
                    'extrainfo': info.get('extrainfo', 'N/A')
                })
        print(f"[INFO] Puertos abiertos detectados: {open_ports}")
        return render_template('results.html', open_ports=open_ports)
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

    responses = "La funcionalidad de generación de información no está disponible en este momento."
    
    if openai.api_key:
        try:
            # Solicitar a OpenAI un análisis o respuesta sobre la información proporcionada
            solicitud = f"Análisis del puerto {port} con producto {product}, versión {version}, extra: {extra_info}."
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=solicitud,
                temperature=0.7,
                max_tokens=150
            )
            responses = response.choices[0].text.strip()
        except Exception as e:
            print(f"[ERROR] Error al obtener respuesta de OpenAI: {e}")
            responses = "Hubo un error al intentar obtener la información de OpenAI."

    return render_template('action.html', port=port, responses=responses, product=product, version=version, extra_info=extra_info)

if __name__ == '__main__':
    print("[INFO] Iniciando la aplicación en modo depuración.")
    app.run(debug=True, port=5200)
