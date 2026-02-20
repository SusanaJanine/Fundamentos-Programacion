def categoria_imc(imc):
    if imc <= 18.5:
        return "Bajo peso"
    elif imc <= 25:
        return "Normal"
    elif imc <= 30:
        return "Sobrepeso"
    else:
        return "Obesidad"
    
def recomendacion_por_categoria(recomendacion):
    if recomendacion == "Bajo peso":
        return "Aumentar ingesta calórica, consumir mas proteinas y carbohidratos. Se recomienda consultar a un nutricionista."
    elif recomendacion == "Normal":
        return "Mantener hábitos saludables y hacer actividad física regular."
    elif recomendacion == "Sobrepeso":
        return "Reducir el consumo de azúcares y calorias, se recomienda hacer ejercicio."
    elif recomendacion == "Obesidad":
        return "Se recomienda mejorar estilo de vida, hacer mas ejercicio y consultar a un nutriologo para la creacion de una dieta especial de defici calorico."