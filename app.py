
from flask import Flask, render_template
import os

app = Flask(__name__)

# Pasta das imagens
STATIC_FOLDER = os.path.join(app.root_path, "static")


def find_image(prefixes):
    """Encontra automaticamente uma imagem existente na pasta static."""
    files = os.listdir(STATIC_FOLDER)

    for prefix in prefixes:
        for filename in files:
            if filename.lower().startswith(prefix.lower()):
                return filename

    return ""


products = [

    # 1. BLAZER
    {
        "id": "blazer",
        "name": "The Tailored Blazer",
        "category": "TAILORING",
        "price": None,
        "image": "blazer.jpg.jpg",
        "description": "Um blazer estruturado com linhas elegantes e um detalhe dourado.",

        "color_images": {
            "Azul-marinho": {
                "frente": "blazer_azul_marinho_frente.jpg",
                "costas": "blazer_azul_marinho_costas.jpg",
                "lado": "blazer_azul_marinho_lado.jpg"
            },
            "Marfim": {
                "frente": "blazer_marfim_frente.jpg",
                "costas": "blazer_marfim_costas.jpg",
                "lado": "blazer_marfim_lado.jpg"
            },
            "Preto": {
                "frente": "blazer_preto_frente.jpg",
                "costas": "blazer_preto_costas.jpg",
                "lado": "blazer_preto_lado.jpg"
            }
        },

        "sizes": ["XS", "S", "M", "L", "XL"]
    },

    # 2. SAIA
    {
        "id": "skirt",
        "name": "The Signature Skirt",
        "category": "SKIRTS",
        "price": None,
        "image": find_image(["saia"]),
        "description": "Uma saia sofisticada para diferentes ocasiões.",
        "sizes": ["XS", "S", "M", "L", "XL"]
    },

    # 3. BODY
    {
        "id": "body",
        "name": "The Lace Body",
        "category": "BODYSUITS",
        "price": None,
        "image": find_image(["body"]),
        "description": "Um body de renda com acabamento delicado.",
        "sizes": ["XS", "S", "M", "L", "XL"]
    },

    # 4. CALÇAS
    {
        "id": "trousers",
        "name": "The Tailored Trousers",
        "category": "TAILORING",
        "price": None,
        "image": find_image(["calcas", "calças", "trousers"]),
        "description": "Calças de corte elegante e acabamento sofisticado.",
        "sizes": ["XS", "S", "M", "L", "XL"]
    },

    # 5. TOP DE MANGA COMPRIDA
    {
        "id": "long-top",
        "name": "The Essential Long Sleeve Top",
        "category": "TOPS",
        "price": None,
        "image": find_image(["top_manga", "top-manga", "long_top"]),
        "description": "Um top de manga comprida com um design elegante.",
        "sizes": ["XS", "S", "M", "L", "XL"]
    },

    # 6. CASACO
    {
        "id": "coat",
        "name": "The Statement Coat",
        "category": "OUTERWEAR",
        "price": None,
        "image": find_image(["casaco", "coat"]),
        "description": "Um casaco sofisticado para completar qualquer conjunto.",
        "sizes": ["XS", "S", "M", "L", "XL"]
    },

    # 7. TOP
    {
        "id": "top",
        "name": "The Essential Top",
        "category": "TOPS",
        "price": None,
        "image": find_image(["top"]),
        "description": "Um top minimalista e versátil.",
        "sizes": ["XS", "S", "M", "L", "XL"]
    }

]


@app.route("/")
def home():
    return render_template("index.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)
