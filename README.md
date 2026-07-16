# Recicla-AI ♻️

Sistema de Inteligência Artificial para classificação automática de resíduos recicláveis utilizando Visão Computacional e Deep Learning.

## 📖 Sobre o Projeto

O **Recicla-AI** é um projeto desenvolvido para a disciplina de Inteligência Artificial. Seu principal objetivo é identificar automaticamente o tipo de resíduo reciclável presente em uma imagem, auxiliando e otimizando processos de triagem, coleta seletiva e reciclagem.

O sistema utiliza técnicas de **Transfer Learning (Aprendizado por Transferência)** baseadas na arquitetura **MobileNetV2**, alcançando alta precisão mesmo com um conjunto de dados otimizado.

## 🎯 Objetivos

- Classificar resíduos recicláveis por imagem.
- Auxiliar a coleta seletiva.
- Aplicar técnicas de Visão Computacional.
- Desenvolver uma aplicação prática utilizando Inteligência Artificial.

### Categorias de Resíduos Suportadas:
- 📄 **Papel / Papelão** (`cardboard`)
- 🧴 **Plástico** (`plastic`)
- 🍾 **Vidro** (`glass`)
- 🥫 **Metal** (`metal`)

---

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python
- **Deep Learning & IA:** TensorFlow, Keras, Scikit-Learn
- **Manipulação de Imagens:** OpenCV, Pillow
- **Web & Interface:** Flask, HTML, CSS
- **Visualização de Dados:** Matplotlib, Pandas
- **Ferramentas de Desenvolvimento:** Jupyter Notebook

---

## 📁 Estrutura do Dataset

Para treinar e testar o modelo, o projeto espera que as imagens estejam organizadas na raiz do projeto dentro de uma pasta chamada `dataset/`, dividida da seguinte forma:

```text
dataset/
├── train/              # Imagens utilizadas para o treino (com Data Augmentation)
│   ├── cardboard/
│   ├── glass/
│   ├── metal/
│   └── plastic/
├── validation/         # Imagens utilizadas para validação durante o treino
│   ├── cardboard/
│   ├── glass/
│   ├── metal/
│   └── plastic/
└── test/               # Imagens para o teste e avaliação final do modelo
    ├── cardboard/
    ├── glass/
    ├── metal/
    └── plastic/
```
---

## Execute a aplicação

Inicie o servidor Flask:

```bash
python app.py
```

O sistema estará disponível em:

```text
http://127.0.0.1:5000
```

---

## Utilizando o sistema

1. Acesse a aplicação pelo navegador.
2. Selecione uma imagem de um resíduo reciclável.
3. Clique em **Classificar**.
4. O sistema exibirá:
   - ♻️ Categoria identificada;
   - 📊 Nível de confiança da previsão.

---


## 🛠 Tecnologias

- Python
- TensorFlow
- Keras
- OpenCV
- NumPy
- Flask
- HTML
- CSS

---

## 👨‍💻 Equipe
- Elton Braian
- Kevin Farias
- Vitória Ataide
- Hudson Jesus
  
---

## 📄 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.
