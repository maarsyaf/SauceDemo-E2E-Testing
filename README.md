# 🧪 SauceDemo Web UI Automation Testing Portfolio

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.15-green.svg)
![Framework](https://img.shields.io/badge/Framework-Unittest-orange.svg)
![Architecture](https://img.shields.io/badge/Architecture-Page%20Object%20Model%20(POM)-purple.svg)

Proyek ini merupakan **Web UI Test Automation Framework** berbasis Python dan Selenium WebDriver yang dikembangkan untuk menguji aplikasi e-commerce [SauceDemo](https://www.saucedemo.com/). Framework ini dirancang berstandar industri menggunakan arsitektur **Page Object Model (POM)** dan metode **Data-Driven Testing (DDT)**.

---

## 🎯 Key Portfolio Features

- **Page Object Model (POM)**: Memisahkan *Page Locators/Actions* dan *Test Script Logic* untuk kustomisasi dan maintenance yang bersih.
- **Data-Driven Testing (DDT)**: Menggunakan data JSON (`login_data.json` & `checkout_data.json`) untuk pengujian skenario masif.
- **Robust Synchronization**: Menggunakan `WebDriverWait` (Explicit Wait) untuk kestabilan eksekusi tes.
- **Comprehensive Coverage**: Mencakup skenario **Positive**, **Negative**, hingga **Edge Cases** (Direct URL bypass, delay handling, dan sinkronisasi state).

---

## 📂 Project Architecture

```text
SauceDemo-E2E-Testing/
├── .gitignore
├── requirements.txt
├── README.md
├── data/
│   ├── login_data.json
│   └── checkout_data.json
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   └── checkout_complete_page.py
└── tests/
    ├── test_login.py
    ├── test_catalog_cart.py
    ├── test_checkout.py
    ├── test_edge_cases.py
    └── test_e2e.py