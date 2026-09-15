import plotly.graph_objects as go
import pandas as pd
import numpy as np

# ==========================================
# 1. ГЕНЕРАЦИЯ ДАННЫХ (Замените на свои)
# ==========================================
# Создаем временную шкалу (даты)
dates = pd.to_datetime([
    '2026-06-05', '2026-06-07', '2026-06-09',
    '2026-06-12', '2026-06-14', '2026-06-16'
])

# 4 последовательности данных (time-series)
# Обратите внимание на масштаб данных: чтобы они красиво пересекались на графике,
# мы будем использовать разные невидимые оси Y для каждой метрики.
data_cost = [20.0, 35.0, 44.36, 44.36, 50.0, 60.0]  # Area (Желтая область)
data_cpa = [0.5, 0.8, 1.0, 1.23, 1.5, 2.0]  # Bar (Синие столбцы)
data_roi = [180.0, 100.0, 60.0, 161.47, 150.0, 200.0]  # Spline (Зеленая кривая)
data_conv = [10, 20, 30, 36, 40, 50]  # Line (Фиолетовая линия)

# ==========================================
# 2. ПОСТРОЕНИЕ ГРАФИКА
# ==========================================
fig = go.Figure()

# --- Трассировка 1: Area (Cost) ---
fig.add_trace(go.Scatter(
    x=dates,
    y=data_cost,
    mode='lines',
    fill='tozeroy',  # Заливка до нуля
    fillcolor='rgba(253, 224, 71, 0.4)',  # Желтый с прозрачностью
    line=dict(width=0),  # Скрываем саму линию, оставляем только заливку
    name='Cost',
    yaxis='y1',
    hovertemplate="<span style='color:#FDE047'>●</span> Cost: %{y:.2f}<extra></extra>"
))

# --- Трассировка 2: Bar (CPA) ---
fig.add_trace(go.Bar(
    x=dates,
    y=data_cpa,
    marker_color='#3B82F6',  # Синий
    name='CPA',
    yaxis='y2',
    width=3600000 * 24,  # Ширина столбца (в миллисекундах, примерно 1 день)
    hovertemplate="<span style='color:#3B82F6'>●</span> CPA: %{y:.2f}<extra></extra>"
))

# --- Трассировка 3: Spline (ROI confirmed) ---
fig.add_trace(go.Scatter(
    x=dates,
    y=data_roi,
    mode='lines',
    line=dict(color='#22C55E', shape='spline', width=3),  # Зеленый, сглаженный
    name='ROI confirmed',
    yaxis='y3',
    hovertemplate="<span style='color:#22C55E'>●</span> ROI confirmed: %{y:.2f}<extra></extra>"
))

# --- Трассировка 4: Line (Conversions) ---
fig.add_trace(go.Scatter(
    x=dates,
    y=data_conv,
    mode='lines+markers',
    line=dict(color='#A855F7', width=2),  # Фиолетовый
    marker=dict(symbol='square', size=8, color='#A855F7'),  # Квадратные маркеры
    name='Conversions',
    yaxis='y4',
    hovertemplate="<span style='color:#A855F7'>●</span> Conversions: %{y}<extra></extra>"
))

# ==========================================
# 3. НАСТРОЙКА СТИЛЯ И ОСЕЙ (Vibe matching)
# ==========================================
fig.update_layout(
    # Цвета фона как на скриншоте
    paper_bgcolor='#FCE7F3',  # Светло-розовый внешний фон
    plot_bgcolor='#FDF2F8',  # Чуть более светлый внутренний фон

    # Настройка тултипа (всплывающей подсказки)
    hovermode='x unified',  # Объединяет данные всех линий в одну подсказку
    hoverlabel=dict(
        bgcolor="white",
        bordercolor="lightgray",
        font=dict(size=13, color="black", family="Arial"),
        namelength=-1  # Скрываем стандартные имена, используем только hovertemplate
    ),

    # Скрываем стандартные оси, чтобы повторить минималистичный UI
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
        hoverformat='%d.%m.%Y'  # Формат даты в тултипе
    ),
    # Настраиваем 4 невидимые оси Y для правильного масштабирования линий
    yaxis=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False, range=[0, 100]),
    yaxis2=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False, overlaying='y', side='right',
                range=[0, 5]),
    yaxis3=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False, overlaying='y', side='right',
                range=[0, 300]),
    yaxis4=dict(showgrid=False, zeroline=False, showline=False, showticklabels=False, overlaying='y', side='right',
                range=[0, 100]),

    # Отступы
    margin=dict(l=20, r=20, t=40, b=20),
    showlegend=False,  # Скрываем легенду, так как она не видна на скриншоте
    dragmode=False  # Отключаем зум рамкой, чтобы было похоже на статичный UI
)

# Показываем график
fig.show()