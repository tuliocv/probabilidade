import streamlit as st
import random
import math
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Probabilidade Aplicada à Computação",
    page_icon="🎲",
    layout="wide"
)

# =========================================================
# ESTILO VISUAL / UX
# =========================================================

st.markdown("""
<style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #17324D;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        font-size: 1.15rem;
        color: #4A5568;
        margin-bottom: 1.2rem;
    }

    .concept-card {
        padding: 1.1rem;
        border-radius: 14px;
        background-color: #F7FAFC;
        border-left: 6px solid #2B6CB0;
        margin-bottom: 1rem;
    }

    .activity-card {
        padding: 1.1rem;
        border-radius: 14px;
        background-color: #FFFDF7;
        border-left: 6px solid #D69E2E;
        margin-bottom: 1rem;
    }

    .success-card {
        padding: 1rem;
        border-radius: 14px;
        background-color: #F0FFF4;
        border-left: 6px solid #38A169;
        margin-bottom: 1rem;
    }

    .danger-card {
        padding: 1rem;
        border-radius: 14px;
        background-color: #FFF5F5;
        border-left: 6px solid #E53E3E;
        margin-bottom: 1rem;
    }

    .small-text {
        font-size: 0.92rem;
        color: #4A5568;
    }

    .badge-easy {
        background-color: #C6F6D5;
        color: #22543D;
        padding: 0.2rem 0.55rem;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.85rem;
    }

    .badge-medium {
        background-color: #FEEBC8;
        color: #7B341E;
        padding: 0.2rem 0.55rem;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.85rem;
    }

    .badge-hard {
        background-color: #FED7D7;
        color: #742A2A;
        padding: 0.2rem 0.55rem;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================

def inicializar_estado():
    if "acertos" not in st.session_state:
        st.session_state.acertos = 0

    if "respondidas" not in st.session_state:
        st.session_state.respondidas = set()

    if "tentativas" not in st.session_state:
        st.session_state.tentativas = 0


def registrar_resultado(nome_exercicio, acertou):
    if nome_exercicio not in st.session_state.respondidas:
        st.session_state.respondidas.add(nome_exercicio)
        st.session_state.tentativas += 1

        if acertou:
            st.session_state.acertos += 1


def mostrar_feedback(nome_exercicio, acertou, explicacao):
    registrar_resultado(nome_exercicio, acertou)

    if acertou:
        st.success("✅ Correto! Excelente raciocínio.")
    else:
        st.error("❌ Ainda não está correto. Revise o conceito e tente novamente.")

    st.info(explicacao)


def verificar_numero(nome_exercicio, resposta_aluno, resposta_correta, explicacao, tolerancia=0.01):
    if st.button(f"Verificar resposta - {nome_exercicio}"):
        acertou = abs(float(resposta_aluno) - float(resposta_correta)) <= tolerancia
        mostrar_feedback(nome_exercicio, acertou, explicacao)


def verificar_texto(nome_exercicio, resposta_aluno, resposta_correta, explicacao):
    if st.button(f"Verificar resposta - {nome_exercicio}"):
        acertou = resposta_aluno == resposta_correta
        mostrar_feedback(nome_exercicio, acertou, explicacao)


def prob_binomial(n, k, p):
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))


def mostrar_badge(nivel):
    if nivel == "Fácil":
        st.markdown('<span class="badge-easy">Fácil</span>', unsafe_allow_html=True)
    elif nivel == "Médio":
        st.markdown('<span class="badge-medium">Médio</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="badge-hard">Desafio</span>', unsafe_allow_html=True)


def bloco_conceito(titulo, texto):
    st.markdown(f"""
    <div class="concept-card">
        <h4>{titulo}</h4>
        <p>{texto}</p>
    </div>
    """, unsafe_allow_html=True)


def bloco_atividade(titulo, texto):
    st.markdown(f"""
    <div class="activity-card">
        <h4>{titulo}</h4>
        <p>{texto}</p>
    </div>
    """, unsafe_allow_html=True)


inicializar_estado()


# =========================================================
# CABEÇALHO
# =========================================================

st.markdown('<div class="main-title">🎲 Probabilidade Aplicada à Computação</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Exercícios conceituais, cálculos, simulações e desafios progressivos para a aula de hoje.</div>',
    unsafe_allow_html=True
)

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.metric("Questões respondidas", len(st.session_state.respondidas))

with col_b:
    st.metric("Acertos", st.session_state.acertos)

with col_c:
    if len(st.session_state.respondidas) > 0:
        desempenho = st.session_state.acertos / len(st.session_state.respondidas) * 100
    else:
        desempenho = 0
    st.metric("Desempenho", f"{desempenho:.0f}%")

st.progress(min(desempenho / 100, 1.0))

st.divider()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.header("🧭 Trilha da aula")

    st.markdown("""
    Use este app como uma sequência de aprendizagem:

    1. **Comece pelos conceitos**
    2. **Resolva os exercícios fáceis**
    3. **Avance para os cálculos**
    4. **Teste as simulações**
    5. **Finalize com os desafios**
    """)

    st.divider()

    st.header("📌 Fórmulas úteis")

    st.latex(r"P(A) = \frac{n(A)}{n(S)}")
    st.latex(r"P(A \cup B) = P(A) + P(B) - P(A \cap B)")
    st.latex(r"P(A \cap B) = P(A) \cdot P(B)")
    st.latex(r"P(A|B) = \frac{P(A \cap B)}{P(B)}")
    st.latex(r"P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}")

    st.divider()

    if st.button("🔄 Reiniciar progresso"):
        st.session_state.acertos = 0
        st.session_state.respondidas = set()
        st.session_state.tentativas = 0
        st.rerun()


# =========================================================
# ABAS PRINCIPAIS
# =========================================================

aba1, aba2, aba3, aba4, aba5, aba6 = st.tabs([
    "📘 Conceitos",
    "🟢 Exercícios fáceis",
    "🟡 Exercícios médios",
    "🔴 Desafios",
    "💻 Simulações",
    "🧰 Calculadoras"
])


# =========================================================
# ABA 1 - CONCEITOS
# =========================================================

with aba1:
    st.header("📘 Resumo dos principais conceitos")

    col1, col2 = st.columns(2)

    with col1:
        bloco_conceito(
            "Experimento aleatório",
            "É uma situação cujo resultado não pode ser previsto com certeza antes de acontecer. Exemplo: lançar um dado, enviar um pacote pela rede ou verificar se um usuário clicará em um anúncio."
        )

        bloco_conceito(
            "Espaço amostral",
            "É o conjunto de todos os resultados possíveis de um experimento. No lançamento de um dado: S = {1, 2, 3, 4, 5, 6}."
        )

        bloco_conceito(
            "Evento",
            "É um subconjunto do espaço amostral. Exemplo: sair número par no dado: A = {2, 4, 6}."
        )

    with col2:
        bloco_conceito(
            "Probabilidade clássica",
            "É usada quando todos os resultados são igualmente prováveis. Calculamos dividindo os casos favoráveis pelo total de casos possíveis."
        )

        bloco_conceito(
            "Probabilidade condicional",
            "Calcula a chance de um evento acontecer sabendo que outro evento já ocorreu. Exemplo: probabilidade de compra dado que o usuário clicou no anúncio."
        )

        bloco_conceito(
            "Eventos independentes",
            "Dois eventos são independentes quando a ocorrência de um não altera a probabilidade do outro."
        )

    st.subheader("🧠 Mapa mental rápido")

    dados_mapa = pd.DataFrame({
        "Conceito": [
            "Probabilidade clássica",
            "Regra da adição",
            "Regra da multiplicação",
            "Probabilidade condicional",
            "Variável discreta",
            "Variável contínua",
            "Distribuição binomial",
            "Distribuição normal"
        ],
        "Pergunta que responde": [
            "Qual é a chance de um evento?",
            "Qual é a chance de A ou B?",
            "Qual é a chance de A e B?",
            "Qual é a chance de A sabendo que B ocorreu?",
            "Estou contando quantidades?",
            "Estou medindo valores em intervalo?",
            "Tenho sucessos e fracassos?",
            "Tenho valores contínuos próximos de uma média?"
        ],
        "Exemplo em Computação": [
            "Chance de sair um número em um sorteio",
            "Erro de login ou falha de conexão",
            "Dois pacotes chegarem corretamente",
            "Compra após clique em anúncio",
            "Número de pacotes perdidos",
            "Tempo de resposta do servidor",
            "Transmissões com sucesso ou falha",
            "Latência de rede"
        ]
    })

    st.dataframe(dados_mapa, use_container_width=True, hide_index=True)


# =========================================================
# ABA 2 - EXERCÍCIOS FÁCEIS
# =========================================================

with aba2:
    st.header("🟢 Exercícios fáceis")
    st.caption("Objetivo: reconhecer conceitos básicos e aplicar cálculos diretos.")

    # Exercício 1
    st.subheader("Exercício 1 — Probabilidade clássica")
    mostrar_badge("Fácil")

    st.markdown("""
    Um dado comum é lançado uma vez.

    Qual é a probabilidade de sair o número **6**?

    Responda em forma decimal.  
    Exemplo: 0.50 para 50%.
    """)

    resposta1 = st.number_input(
        "Digite sua resposta:",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="ex1"
    )

    verificar_numero(
        "Exercício 1",
        resposta1,
        1 / 6,
        """
        Em um dado comum, existem 6 resultados possíveis e apenas 1 resultado favorável: sair o número 6.

        P(6) = 1/6 ≈ 0,1667

        Portanto, a probabilidade é aproximadamente 16,67%.
        """,
        tolerancia=0.01
    )

    st.divider()

    # Exercício 2
    st.subheader("Exercício 2 — Evento")
    mostrar_badge("Fácil")

    st.markdown("""
    No lançamento de um dado, considere o evento:

    **A = sair um número par**

    Qual conjunto representa corretamente esse evento?
    """)

    resposta2 = st.radio(
        "Escolha a alternativa correta:",
        [
            "{1, 2, 3}",
            "{2, 4, 6}",
            "{1, 3, 5}",
            "{4, 5, 6}"
        ],
        key="ex2"
    )

    verificar_texto(
        "Exercício 2",
        resposta2,
        "{2, 4, 6}",
        """
        Os números pares em um dado comum são 2, 4 e 6.

        Portanto, o evento A é:

        A = {2, 4, 6}
        """
    )

    st.divider()

    # Exercício 3
    st.subheader("Exercício 3 — Evento impossível e evento certo")
    mostrar_badge("Fácil")

    st.markdown("""
    Ao lançar um dado comum, qual é a probabilidade de sair um número maior que 6?
    """)

    resposta3 = st.number_input(
        "Digite sua resposta:",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.2f",
        key="ex3"
    )

    verificar_numero(
        "Exercício 3",
        resposta3,
        0,
        """
        Em um dado comum, os resultados possíveis são apenas:

        {1, 2, 3, 4, 5, 6}

        Não existe resultado maior que 6. Portanto, é um evento impossível.

        P(A) = 0
        """
    )

    st.divider()

    # Exercício 4
    st.subheader("Exercício 4 — Variável discreta ou contínua?")
    mostrar_badge("Fácil")

    st.markdown("""
    O **número de usuários conectados simultaneamente** em um servidor é uma variável:
    """)

    resposta4 = st.radio(
        "Escolha a alternativa correta:",
        [
            "Discreta",
            "Contínua"
        ],
        key="ex4"
    )

    verificar_texto(
        "Exercício 4",
        resposta4,
        "Discreta",
        """
        O número de usuários é uma contagem: 0, 1, 2, 3, 4...

        Como não faz sentido ter 3,7 usuários conectados, essa variável é discreta.
        """
    )


# =========================================================
# ABA 3 - EXERCÍCIOS MÉDIOS
# =========================================================

with aba3:
    st.header("🟡 Exercícios médios")
    st.caption("Objetivo: aplicar regras da adição, multiplicação e probabilidade condicional.")

    # Exercício 5
    st.subheader("Exercício 5 — Regra da adição")
    mostrar_badge("Médio")

    st.markdown("""
    No lançamento de um dado, considere:

    A = sair número par = {2, 4, 6}  
    B = sair número maior que 4 = {5, 6}

    Qual é a probabilidade de sair número par **ou** número maior que 4?

    Responda em decimal.
    """)

    resposta5 = st.number_input(
        "Digite sua resposta:",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="ex5"
    )

    verificar_numero(
        "Exercício 5",
        resposta5,
        4 / 6,
        """
        A = {2, 4, 6}

        B = {5, 6}

        A união B = {2, 4, 5, 6}

        Temos 4 resultados favoráveis em 6 possíveis.

        P(A ∪ B) = 4/6 ≈ 0,6667

        Atenção: o número 6 aparece nos dois eventos e não deve ser contado duas vezes.
        """,
        tolerancia=0.01
    )

    st.divider()

    # Exercício 6
    st.subheader("Exercício 6 — Regra da multiplicação")
    mostrar_badge("Médio")

    st.markdown("""
    Uma rede transmite pacotes com **90% de chance de sucesso**.

    Considerando transmissões independentes, qual é a probabilidade de **3 pacotes** chegarem corretamente?

    Responda em decimal.
    """)

    resposta6 = st.number_input(
        "Digite sua resposta:",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="ex6"
    )

    verificar_numero(
        "Exercício 6",
        resposta6,
        0.9 ** 3,
        """
        Como os eventos são independentes, multiplicamos as probabilidades:

        P = 0,9 × 0,9 × 0,9

        P = 0,729

        Portanto, a probabilidade é 72,9%.
        """,
        tolerancia=0.01
    )

    st.divider()

    # Exercício 7
    st.subheader("Exercício 7 — Pelo menos uma falha")
    mostrar_badge("Médio")

    st.markdown("""
    Uma rede transmite pacotes com **95% de chance de sucesso**.

    Três pacotes serão enviados.

    Qual é a probabilidade de **pelo menos um pacote falhar**?

    Responda em decimal.
    """)

    resposta7 = st.number_input(
        "Digite sua resposta:",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="ex7"
    )

    resposta_correta7 = 1 - (0.95 ** 3)

    verificar_numero(
        "Exercício 7",
        resposta7,
        resposta_correta7,
        """
        Para calcular 'pelo menos uma falha', é mais fácil usar o complemento.

        Primeiro calculamos a chance de todos os pacotes chegarem corretamente:

        P(todos corretos) = 0,95³ = 0,857375

        Depois:

        P(pelo menos uma falha) = 1 - 0,857375

        P ≈ 0,1426

        Portanto, a chance é aproximadamente 14,26%.
        """,
        tolerancia=0.01
    )

    st.divider()

    # Exercício 8
    st.subheader("Exercício 8 — Probabilidade condicional")
    mostrar_badge("Médio")

    st.markdown("""
    Uma loja virtual registrou:

    - 500 visitantes
    - 120 clicaram em uma promoção
    - 30 compraram
    - 24 compraram após clicar na promoção

    Qual é a probabilidade de compra **dado que o usuário clicou na promoção**?

    Responda em decimal.
    """)

    resposta8 = st.number_input(
        "Digite sua resposta:",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="ex8"
    )

    verificar_numero(
        "Exercício 8",
        resposta8,
        24 / 120,
        """
        Queremos calcular:

        P(compra | clique)

        Entre os 120 usuários que clicaram, 24 compraram.

        P(compra | clique) = 24 / 120 = 0,20

        Portanto, 20% dos usuários que clicaram compraram.
        """,
        tolerancia=0.01
    )

    st.divider()

    # Exercício 9
    st.subheader("Exercício 9 — Escolha da distribuição")
    mostrar_badge("Médio")

    st.markdown("""
    Em um sistema de comunicação digital, cada pacote transmitido pode ter dois resultados:

    - sucesso
    - falha

    O sistema envia 20 pacotes e queremos calcular a probabilidade de exatamente 18 chegarem corretamente.

    Qual distribuição é mais adequada?
    """)

    resposta9 = st.radio(
        "Escolha a alternativa correta:",
        [
            "Distribuição normal",
            "Distribuição binomial",
            "Distribuição uniforme",
            "Nenhuma distribuição se aplica"
        ],
        key="ex9"
    )

    verificar_texto(
        "Exercício 9",
        resposta9,
        "Distribuição binomial",
        """
        A distribuição binomial é adequada porque:

        - existe número fixo de tentativas;
        - cada tentativa tem dois resultados: sucesso ou falha;
        - a probabilidade de sucesso é constante;
        - as tentativas são consideradas independentes.
        """
    )


# =========================================================
# ABA 4 - DESAFIOS
# =========================================================

with aba4:
    st.header("🔴 Desafios")
    st.caption("Objetivo: integrar conceitos, cálculos e interpretação em contextos de Computação.")

    # Exercício 10
    st.subheader("Exercício 10 — Sistema de autenticação")
    mostrar_badge("Desafio")

    st.markdown("""
    Um sistema permite até **3 tentativas de login**.

    A chance de o usuário digitar a senha corretamente em cada tentativa é de **60%**.

    Considerando as tentativas independentes, qual é a chance de o usuário conseguir acessar o sistema em até 3 tentativas?

    Responda em decimal.
    """)

    resposta10 = st.number_input(
        "Digite sua resposta:",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="ex10"
    )

    resposta_correta10 = 1 - (0.4 ** 3)

    verificar_numero(
        "Exercício 10",
        resposta10,
        resposta_correta10,
        """
        A chance de erro em uma tentativa é:

        1 - 0,60 = 0,40

        A chance de errar as 3 tentativas é:

        0,40³ = 0,064

        Logo, a chance de conseguir acessar em até 3 tentativas é:

        1 - 0,064 = 0,936

        Portanto, a probabilidade é 93,6%.
        """,
        tolerancia=0.01
    )

    st.divider()

    # Exercício 11
    st.subheader("Exercício 11 — Classificador de spam")
    mostrar_badge("Desafio")

    st.markdown("""
    Um sistema analisou 1000 e-mails:

    - 300 eram spam
    - 700 não eram spam
    - entre os spams, 240 tinham a palavra "promoção"
    - entre os não spams, 70 tinham a palavra "promoção"

    Se um e-mail contém a palavra **promoção**, qual é a probabilidade de ele ser spam?

    Responda em decimal.
    """)

    resposta11 = st.number_input(
        "Digite sua resposta:",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="ex11"
    )

    resposta_correta11 = 240 / (240 + 70)

    verificar_numero(
        "Exercício 11",
        resposta11,
        resposta_correta11,
        """
        Queremos calcular:

        P(spam | contém promoção)

        Total de e-mails com a palavra promoção:

        240 + 70 = 310

        Desses, 240 eram spam.

        P(spam | promoção) = 240 / 310 ≈ 0,774

        Portanto, a probabilidade é aproximadamente 77,4%.
        """,
        tolerancia=0.01
    )

    st.divider()

    # Exercício 12
    st.subheader("Exercício 12 — Distribuição binomial")
    mostrar_badge("Desafio")

    st.markdown("""
    Uma rede envia 5 pacotes.

    Cada pacote tem 80% de chance de chegar corretamente.

    Qual é a probabilidade de exatamente **4 pacotes** chegarem corretamente?

    Responda em decimal.
    """)

    resposta12 = st.number_input(
        "Digite sua resposta:",
        min_value=0.0,
        max_value=1.0,
        step=0.01,
        format="%.4f",
        key="ex12"
    )

    resposta_correta12 = prob_binomial(5, 4, 0.8)

    verificar_numero(
        "Exercício 12",
        resposta12,
        resposta_correta12,
        """
        Usamos a fórmula da distribuição binomial:

        P(X = k) = C(n,k) × p^k × (1-p)^(n-k)

        Neste caso:

        n = 5  
        k = 4  
        p = 0,8

        P(X = 4) = C(5,4) × 0,8⁴ × 0,2¹

        P(X = 4) = 5 × 0,4096 × 0,2

        P(X = 4) = 0,4096

        Portanto, a probabilidade é 40,96%.
        """,
        tolerancia=0.01
    )

    st.divider()

    # Exercício 13
    st.subheader("Exercício 13 — Análise crítica")
    mostrar_badge("Desafio")

    st.markdown("""
    Um professor deseja modelar o **tempo de resposta** de um sistema web em milissegundos.

    Qual tipo de variável está sendo analisada?
    """)

    resposta13 = st.radio(
        "Escolha a alternativa correta:",
        [
            "Variável discreta, porque tempo é sempre inteiro",
            "Variável contínua, porque tempo é uma medida em intervalo",
            "Variável binomial, porque só existem dois resultados",
            "Variável impossível de modelar"
        ],
        key="ex13"
    )

    verificar_texto(
        "Exercício 13",
        resposta13,
        "Variável contínua, porque tempo é uma medida em intervalo",
        """
        O tempo de resposta é uma medida.

        Ele pode assumir valores como:

        120 ms, 120,5 ms, 120,57 ms etc.

        Portanto, é uma variável contínua.
        """
    )


# =========================================================
# ABA 5 - SIMULAÇÕES
# =========================================================

with aba5:
    st.header("💻 Simulações computacionais")
    st.caption("Objetivo: visualizar a probabilidade na prática.")

    st.subheader("Simulação 1 — Lançamento de dado")

    col1, col2 = st.columns([1, 2])

    with col1:
        n_lancamentos = st.slider(
            "Número de lançamentos:",
            min_value=10,
            max_value=10000,
            value=1000,
            step=10
        )

        simular_dado = st.button("🎲 Simular dado")

    with col2:
        if simular_dado:
            resultados = [random.randint(1, 6) for _ in range(n_lancamentos)]
            contagens = {i: resultados.count(i) for i in range(1, 7)}

            df_dado = pd.DataFrame({
                "Número": list(contagens.keys()),
                "Frequência": list(contagens.values()),
                "Probabilidade observada": [contagens[i] / n_lancamentos for i in range(1, 7)]
            })

            st.dataframe(df_dado, use_container_width=True, hide_index=True)

            fig, ax = plt.subplots()
            ax.bar(df_dado["Número"], df_dado["Probabilidade observada"])
            ax.axhline(1 / 6, linestyle="--", label="Probabilidade teórica")
            ax.set_xlabel("Resultado do dado")
            ax.set_ylabel("Probabilidade observada")
            ax.set_title("Simulação de lançamentos de dado")
            ax.legend()

            st.pyplot(fig)

            st.info("""
            Quanto maior o número de lançamentos, mais a probabilidade observada tende a se aproximar da probabilidade teórica de 1/6.
            """)

    st.divider()

    st.subheader("Simulação 2 — Perda de pacotes em rede")

    col3, col4, col5 = st.columns(3)

    with col3:
        qtd_pacotes = st.number_input(
            "Quantidade de pacotes por operação:",
            min_value=1,
            max_value=50,
            value=10,
            step=1
        )

    with col4:
        prob_sucesso = st.slider(
            "Probabilidade de sucesso por pacote:",
            min_value=0.0,
            max_value=1.0,
            value=0.90,
            step=0.01
        )

    with col5:
        qtd_simulacoes = st.number_input(
            "Número de simulações:",
            min_value=100,
            max_value=50000,
            value=10000,
            step=100
        )

    if st.button("📡 Simular transmissão"):
        sucesso_total = 0

        for _ in range(qtd_simulacoes):
            operacao_ok = True

            for _ in range(qtd_pacotes):
                if random.random() > prob_sucesso:
                    operacao_ok = False

            if operacao_ok:
                sucesso_total += 1

        prob_observada = sucesso_total / qtd_simulacoes
        prob_teorica = prob_sucesso ** qtd_pacotes

        col_result1, col_result2, col_result3 = st.columns(3)

        with col_result1:
            st.metric("Probabilidade simulada", f"{prob_observada:.2%}")

        with col_result2:
            st.metric("Probabilidade teórica", f"{prob_teorica:.2%}")

        with col_result3:
            st.metric("Risco de pelo menos uma falha", f"{1 - prob_teorica:.2%}")

        st.info("""
        Esta simulação mostra que, mesmo quando a chance individual de sucesso é alta, a chance de todos os pacotes chegarem corretamente pode cair bastante quando muitos pacotes são necessários.
        """)


# =========================================================
# ABA 6 - CALCULADORAS
# =========================================================

with aba6:
    st.header("🧰 Calculadoras de apoio")
    st.caption("Use as calculadoras para conferir os cálculos dos exercícios.")

    calc1, calc2, calc3 = st.columns(3)

    with calc1:
        st.subheader("Probabilidade clássica")

        casos_favoraveis = st.number_input(
            "Casos favoráveis:",
            min_value=0,
            value=1,
            step=1,
            key="calc_fav"
        )

        casos_possiveis = st.number_input(
            "Casos possíveis:",
            min_value=1,
            value=6,
            step=1,
            key="calc_poss"
        )

        if casos_favoraveis <= casos_possiveis:
            prob = casos_favoraveis / casos_possiveis
            st.success(f"P(A) = {prob:.4f} = {prob:.2%}")
        else:
            st.warning("Os casos favoráveis não podem ser maiores que os casos possíveis.")

    with calc2:
        st.subheader("Eventos independentes")

        p_a = st.number_input(
            "P(A):",
            min_value=0.0,
            max_value=1.0,
            value=0.9,
            step=0.01,
            key="calc_pa"
        )

        p_b = st.number_input(
            "P(B):",
            min_value=0.0,
            max_value=1.0,
            value=0.9,
            step=0.01,
            key="calc_pb"
        )

        prob_ab = p_a * p_b
        st.success(f"P(A ∩ B) = {prob_ab:.4f} = {prob_ab:.2%}")

    with calc3:
        st.subheader("Binomial")

        n = st.number_input(
            "n: número de tentativas",
            min_value=1,
            max_value=100,
            value=5,
            step=1,
            key="calc_bin_n"
        )

        k = st.number_input(
            "k: número de sucessos",
            min_value=0,
            max_value=100,
            value=4,
            step=1,
            key="calc_bin_k"
        )

        p = st.number_input(
            "p: probabilidade de sucesso",
            min_value=0.0,
            max_value=1.0,
            value=0.8,
            step=0.01,
            key="calc_bin_p"
        )

        if k <= n:
            resultado_binomial = prob_binomial(n, k, p)
            st.success(f"P(X = {k}) = {resultado_binomial:.4f} = {resultado_binomial:.2%}")
        else:
            st.warning("O número de sucessos k não pode ser maior que o número de tentativas n.")

    st.divider()

    st.subheader("📊 Comparador rápido: binomial x normal")

    df_comp = pd.DataFrame({
        "Pergunta": [
            "Estou contando sucessos?",
            "Tenho apenas sucesso ou fracasso?",
            "Tenho número fixo de tentativas?",
            "Estou medindo tempo, latência ou temperatura?",
            "Os valores se concentram em torno de uma média?"
        ],
        "Se sim, pense em": [
            "Binomial",
            "Binomial",
            "Binomial",
            "Normal",
            "Normal"
        ]
    })

    st.dataframe(df_comp, use_container_width=True, hide_index=True)


# =========================================================
# FECHAMENTO
# =========================================================

st.divider()

st.header("📌 Conclusão da atividade")

if desempenho >= 80:
    st.markdown("""
    <div class="success-card">
        <h4>Excelente desempenho!</h4>
        <p>Você demonstrou boa compreensão dos conceitos de probabilidade, regras de cálculo e aplicações em Computação.</p>
    </div>
    """, unsafe_allow_html=True)
elif desempenho >= 50:
    st.markdown("""
    <div class="activity-card">
        <h4>Bom caminho!</h4>
        <p>Você já compreendeu parte dos conceitos. Revise principalmente os exercícios de probabilidade condicional, eventos independentes e distribuição binomial.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="danger-card">
        <h4>Continue praticando!</h4>
        <p>Comece novamente pela aba de conceitos e depois resolva os exercícios fáceis antes de avançar para os desafios.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
### Roteiro mental para resolver problemas de probabilidade

1. Identifique o experimento aleatório.  
2. Determine o espaço amostral.  
3. Identifique o evento de interesse.  
4. Veja se os resultados são igualmente prováveis.  
5. Verifique se os eventos são independentes ou condicionais.  
6. Escolha a regra ou distribuição adequada.  
7. Interprete o resultado no contexto do problema.
""")

st.success("Fim da atividade. Revise os exercícios em que teve mais dificuldade e refaça as simulações com outros valores.")
