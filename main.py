from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import subprocess

app = FastAPI(title="Hello World App")

def build_astro():
    """Build Astro à chaque lancement"""
    print("🚀 Building Astro...")
    try:
        # Aller dans le dossier Astro et builder
        original_dir = os.getcwd()
        os.chdir("astro-frontend")
        subprocess.run(["npm", "run", "build"], check=True)
        os.chdir(original_dir)
        print("✅ Build Astro réussi!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors du build Astro: {e}")
        os.chdir(original_dir)
    except FileNotFoundError:
        print("❌ Dossier astro-frontend introuvable")
        os.chdir(original_dir)

# Build automatique au démarrage
build_astro()

# Monter les dossiers statiques
if os.path.exists("astro-frontend/dist/assets"):
    app.mount("/assets", StaticFiles(directory="astro-frontend/dist/assets"), name="assets")

if os.path.exists("astro-frontend/dist/_astro"):
    app.mount("/_astro", StaticFiles(directory="astro-frontend/dist/_astro"), name="astro")

if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Route principale - sert le fichier Astro
@app.get("/")
async def read_index():
    if os.path.exists("astro-frontend/dist/index.html"):
        return FileResponse("astro-frontend/dist/index.html")
    else:
        return {"error": "Astro build not found."}

# Route pour les autres pages Astro
@app.get("/{path_name:path}")
async def read_astro_pages(path_name: str):
    file_path = f"astro-frontend/dist/{path_name}"
    
    # Si c'est un fichier qui existe, le servir
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    
    # Pour le routing côté client, servir index.html
    if os.path.exists("astro-frontend/dist/index.html"):
        return FileResponse("astro-frontend/dist/index.html")
    else:
        return {"error": "Astro build not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)