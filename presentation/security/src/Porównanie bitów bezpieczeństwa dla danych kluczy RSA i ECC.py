import plotly.express as px
import pandas as pd

data = {
    "Bity bezpieczeństwa": [75, 100, 125, 150, 175] * 2,
    "Wielkość klucza (bits)": [
        1024, 2048, 3072, 7680, 15360,  # RSA
        160, 224, 256, 384, 512  # ECC
    ],
    "Algorytm": ["RSA"] * 5 + ["ECC"] * 5
}

df = pd.DataFrame(data)

fig = px.bar(
    df, x="Bity bezpieczeństwa", y="Wielkość klucza (bits)", color="Algorytm",
    barmode="group",
    title="Porównanie bitów bezpieczeństwa dla danych kluczy RSA i ECC",
    log_y=True
)

fig.show()
