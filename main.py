from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Elon Musk afirma que as redes sociais são projetadas para nos manter dentro da plataforma, para que passemos o máximo de tempo possível visualizando conteúdo.",            
              "De acordo com um estudo realizado em 2018, mais de 50% das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones.", 
              "As redes sociais têm seus pontos positivos e negativos, e devemos estar conscientes de ambos ao utilizá-las.", 
              "O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna."]


@app.route("/portugues")
def portugues():
    return f'<h1>Língua portuguesa</h1><p>O português é a língua oficial de nove países, sendo eles: Angola, Brasil, Cabo Verde, Guiné-Bissau, Guiné Equatorial, Moçambique, Portugal, São Tomé e Princípe e Timor-Leste.</p>'

@app.route("/curiosidade")
def curiosidade():
    fato = random.choice(facts_list)
    return f"<h1>Você sabia?</h1><p>{fato}</p>"

if __name__ == "__main__":
    app.run(debug=True)
