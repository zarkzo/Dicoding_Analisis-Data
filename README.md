# Dashboard Streamlit untuk Analisis Penjualan 

## Setup Environment - Anaconda
```
conda create --name dashboard-env python=3.12
conda activate dashboard-env
pip install -r requirements.txt
```

## Setup Environment - VS Code
```
mkdir dashboard_streamlit
cd dashboard_streamlit
python -m venv venv
venv\Scripts\activate  # Untuk Windows
source venv/bin/activate  # Untuk Mac/Linux
pip install -r requirements.txt
```

## Install Dataset dari Kaggle
```
!pip install opendatasets
import opendatasets as od
od.download("https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce/data")
```

## Menjalankan Aplikasi Streamlit
```
streamlit run app.py
```

