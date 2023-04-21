{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNNSaidRkftwEQ5mknXcqgb",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SebSchr92/TestRep/blob/main/Import_Utils.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "UmJi5c3qXiAv"
      },
      "outputs": [],
      "source": [
        "!pip install Historic-Crypto\n",
        "from Historic_Crypto import HistoricalData\n",
        "from Historic_Crypto import LiveCryptoData\n",
        "from Historic_Crypto import Cryptocurrencies\n",
        "import datetime\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import itertools\n",
        "import numpy as np\n",
        "import plotly.graph_objects as go\n",
        "import gzip\n",
        "import io\n",
        "\n",
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd '/content/drive/MyDrive/Colab Notebooks/MA/Daten'"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7JhlosAKXxp4",
        "outputId": "6a1d8d1d-56f1-4598-de44-21cf871afbd8"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive/Colab Notebooks/MA/Daten\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Github Token\n",
        "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"
      ],
      "metadata": {
        "id": "e5IbizB3ZexC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def Test():\n",
        "  return None"
      ],
      "metadata": {
        "id": "IU1xJvkVmM7n"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Fetch OHLCV data\n",
        "def fetch_data(ticker='BTC-USD', granularity=60, start_date='2017-07-22-00-00', end_date=None, verbose=False):\n",
        "  df = HistoricalData(ticker, granularity, start_date, end_date, verbose).retrieve_data()\n",
        "  return df\n",
        "\n",
        "\n",
        "def check_raw_data(df, freq='D'):\n",
        "  print('---------------------------------------------')\n",
        "  print(f'Range of Data: {df.index.min()} - {df.index.max()}')\n",
        "  print('---------------------------------------------\\n')\n",
        "  print('---------------------------------------------')\n",
        "  if df.isna().any().any():\n",
        "    print('There are missing values in the raw data')\n",
        "  else:\n",
        "    print('The raw data is complete')\n",
        "  print('---------------------------------------------\\n')\n",
        "\n",
        "  missing_days = pd.date_range(start=df.index.floor('d').min(), end=df.index.floor('d').max(), freq=freq).difference(df.index.floor('d'))\n",
        "  print('Missing days: ', missing_days.size)\n",
        "  print(missing_days)\n",
        "  print('---------------------------------------------\\n')\n",
        "  print('---------------------------------------------')\n",
        "  print('Shape:', df.shape)\n",
        "  print('---------------------------------------------\\n')\n",
        "\n",
        "\n",
        "def sort_unique(df):\n",
        "  print('---------------------------------------------')\n",
        "  if df.index.is_monotonic_increasing == False:\n",
        "    df.sort_index(inplace=True)\n",
        "  print('Dataset is monotonic increasing')\n",
        "  print('---------------------------------------------\\n')\n",
        "  print('---------------------------------------------')\n",
        "  duplicate_indices = df.index.duplicated(keep=False)\n",
        "  duplicated_df = df[duplicate_indices]\n",
        "  if duplicated_df.shape[0] == 0:\n",
        "    print('The dataset has no duplicate values')\n",
        "    print('---------------------------------------------')\n",
        "    df_ = df\n",
        "  else:\n",
        "    df_ = df[~df.index.duplicated(keep='first')]\n",
        "    print(' Duplicates droped')\n",
        "    print('---------------------------------------------')\n",
        "    print('---------------------------------------------')\n",
        "    print('New Shape:', df_.shape)\n",
        "    print('---------------------------------------------\\n')\n",
        "  return df_\n",
        "\n",
        "\n",
        "def save_data(df, name):\n",
        "  # on Drive\n",
        "  folder_path = '/content/drive/MyDrive/Colab Notebooks/MA/Daten/'\n",
        "  file_path = folder_path + name + '.csv'\n",
        "  df.to_csv(file_path)\n",
        "  # Bestätigungsnachricht ausgeben\n",
        "  print(f\"Die Datei wurde erfolgreich in {file_path} gespeichert.\")\n",
        "\n",
        "  # Environment -> local\n",
        "  #df.to_csv('df_16_17.csv') \n",
        "\n",
        "\n",
        "# Analyze trading volume of each day\n",
        "def vol_per_day(df):\n",
        "  df_by_ = df.groupby(df.index.date)\n",
        "  volume_by_ = df_by_['volume'].sum()\n",
        "  plt.hist(volume_by_, bins=50)\n",
        "  plt.xlabel('Trading Volume')\n",
        "  plt.ylabel('Days')\n",
        "  plt.show()\n",
        "\n"
      ],
      "metadata": {
        "id": "QhkamZlUXq2D"
      },
      "execution_count": 2,
      "outputs": []
    }
  ]
}