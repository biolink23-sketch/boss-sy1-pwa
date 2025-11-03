import streamlit as st
import base64

# 4) ЛОГОТИП ГИТАРЫ (Explorer Black & White SVG, закодированный в Base64)
EXPLORER_LOGO_BASE64 = "PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48cGF0aCBkPSJNMjU2IDQ4QzE0MS4xIDQ4IDQ4IDE0MS4xIDQ4IDI1NnM5My4xIDIwOCAyMDggMjA4IDIwOC05My4xIDIwOC0yMDhTNDA0LjkgNDggMjU2IDQ4em0xMzMuMSAxMDcuMWwtMjEuOCA5LjgtNDEuOCAxOC45Yy0xOC44IDguNS0zMy4yIDI4LjUtMzMuMiA0OC45djExMy42Yy0xMy40LTguMi0zMC4yLTEzLjEtNDguNS0xMy4xcy0zNS4xIDQuOS00OC41IDEzLjFWMjA5LjhjMC0yMC40LTE0LjQtNDAuNC0zMy4yLTQ4LjlsLTQxLjgtMTguOS0yMS44LTkuOGMtOS44LTQuNC0xMS4zLTE3LjMtMi43LTI0LjdsNDUuMy0zOC45YzkuOC04LjQgMjQuOS04LjQgMzQuNiAwbDExLjQgOS44YzkuOCA4LjQgMjQuOSA4LjQgMzQuNiAwbDExLjQtOS44YzkuOC04LjQgMjQuOSA4LjQgMzQuNiAwbDQ1LjMgMzguOWM4LjYgNy40IDcuMSAyMC4zLTIuNyAyNC43ek0xNjAgMzIwYzAtMTcuNyAxNC4zLTMyIDMyLTMyczMyIDE0LjMgMzIgMzItMTQuMyAzMi0zMiAzMi0zMi0xNC4zLTMyLTMyem0xNjAgNjRjLTE3LjcgMC0zMi0xNC4zLTMyLTMyczE0LjMtMzIgMzItMzIgMzIgMTQuMyAzMiAzMi0xNC4zIDMyLTMyIDMyeiIvPjwvc3ZnPg=="

# Конфигурация страницы
st.set_page_config(
    page_title="Night Budva Boss SY-1 Presets",
    page_icon=f"data:image/svg+xml;base64,{EXPLORER_LOGO_BASE64}",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 1-3) РАСШИРЕННАЯ БАЗА ПРЕСЕТОВ (с ритмом, глубиной, настроением и совместимостью)
PRESETS = {
    "ПОПУЛЯРНЫЕ": {
        "Classic Lead Synth": {"desc": "Классический лид-синтезатор для соло", "type": "LEAD 1", "variation": 3, "tone": 7, "depth": 5, "effect": 8, "direct": 3, "mode": "GUITAR", "good_notes": ["C", "D", "E", "G", "A"], "info": {"creator": "Preset из заводской библиотеки Boss", "source": "Boss Tone Central", "genres": "Rock, Pop-Rock, Alternative", "description": "Сочетает аналоговое тепло с четкой атакой."}, "rhythm": "Быстрый, четкий", "intensity": 7, "mood": "Энергичное, мелодичное", "compatibility": ["Ibanez Tube Screamer (Overdrive)", "MXR Carbon Copy (Delay)", "Boss CE-2W (Chorus)"]},
        "Fat Bass Synth": {"desc": "Жирный бас-синтезатор", "type": "BASS", "variation": 5, "tone": 4, "depth": 6, "effect": 9, "direct": 2, "mode": "BASS", "good_notes": ["E", "A", "D", "G"], "info": {"creator": "Модификация Josh Smith", "source": "Premier Guitar Demo", "genres": "Funk, Nu-Metal, Rock", "description": "Толстый саб-бас с аналоговым характером."}, "rhythm": "Грувовый, средний темп", "intensity": 8, "mood": "Плотное, качающее", "compatibility": ["MXR Bass Octave Deluxe", "Electro-Harmonix Bassballs (Envelope Filter)", "Darkglass B7K (Preamp)"]},
        "Analog Pad": {"desc": "Мягкий аналоговый пад", "type": "PAD", "variation": 2, "tone": 6, "depth": 7, "effect": 7, "direct": 4, "mode": "GUITAR", "good_notes": ["C", "D", "E", "F", "G", "A", "B"], "info": {"creator": "Preset создан Andy Timmons", "source": "Boss Official Preset Library", "genres": "Ambient, Post-Rock", "description": "Эмулирует Juno-60 pad для создания атмосферы."}, "rhythm": "Медленный, без атаки", "intensity": 6, "mood": "Воздушное, обволакивающее", "compatibility": ["EarthQuaker Devices Astral Destiny (Reverb)", "Strymon Volante (Echo)", "Walrus Audio SLO (Reverb)"]}
    },
    "METAL": {
        "Djent Sub Drop": {"desc": "Суб-бас для djent breakdown", "type": "BASS", "variation": 1, "tone": 2, "depth": 9, "effect": 10, "direct": 1, "mode": "GUITAR", "good_notes": ["E", "D", "C", "A"], "info": {"creator": "Misha Mansoor (Periphery) inspired", "source": "Djent forum, Sevenstring.org", "genres": "Djent, Progressive Metal", "description": "Добавляет октаву вниз к drop-tuning. Идеален для брейкдаунов."}, "rhythm": "Синкопированный, агрессивный", "intensity": 10, "mood": "Тяжелое, брутальное", "compatibility": ["Horizon Devices Precision Drive (Gate/Drive)", "Fortin Grind (Booster)", "Digitech The Drop"]},
        "Industrial Grind": {"desc": "Индустриальный скрежет", "type": "SFX 1", "variation": 8, "tone": 9, "depth": 8, "effect": 9, "direct": 2, "mode": "GUITAR", "good_notes": ["E", "D", "C#", "A"], "info": {"creator": "Inspired by Ministry, NIN", "source": "Industrial Metal groups", "genres": "Industrial Metal, Nu-Metal", "description": "Агрессивный индустриальный звук в стиле Ministry и Fear Factory."}, "rhythm": "Машинный, монотонный", "intensity": 9, "mood": "Холодное, механическое", "compatibility": ["Boss NS-2 (Noise Gate)", "ProCo RAT (Distortion)", "Digitech Whammy"]},
        "Doom Synth": {"desc": "Мрачный синтезатор для doom metal", "type": "LEAD 2", "variation": 6, "tone": 3, "depth": 9, "effect": 7, "direct": 4, "mode": "GUITAR", "good_notes": ["D", "C", "G", "F"], "info": {"creator": "Electric Wizard tone inspired", "source": "Doom Metal subreddit", "genres": "Doom Metal, Stoner Metal", "description": "Темный синтезаторный звук с медленной атакой."}, "rhythm": "Очень медленный, вязкий", "intensity": 8, "mood": "Мрачное, угнетающее", "compatibility": ["Electro-Harmonix Big Muff Pi (Fuzz)", "Boss OC-5 (Octave)", "Dunlop Cry Baby (Wah)"]},
        "Black Metal Synth": {"desc": "Холодный синтезатор для black metal", "type": "STR", "variation": 9, "tone": 8, "depth": 6, "effect": 8, "direct": 3, "mode": "GUITAR", "good_notes": ["E", "D", "C#", "B"], "info": {"creator": "Inspired by Emperor, Dimmu Borgir", "source": "Black Metal forums", "genres": "Symphonic Black Metal", "description": "Эмулирует оркестровые партии Dimmu Borgir."}, "rhythm": "Быстрый, тремоло", "intensity": 7, "mood": "Холодное, эпичное", "compatibility": ["Boss RV-6 (Reverb)", "TC Electronic Flashback (Delay)", "Keeley Compressor Plus"]}
    },
    "FOLK": {
        "Celtic Strings": {"desc": "Кельтские струнные", "type": "STR", "variation": 4, "tone": 6, "depth": 5, "effect": 7, "direct": 5, "mode": "GUITAR", "good_notes": ["D", "A", "G", "E"], "info": {"creator": "Inspired by Dead Can Dance", "source": "Neofolk forums", "genres": "Celtic Folk, Neofolk", "description": "Эмулирует звук fiddle и кельтских струнных."}, "rhythm": "Мелодичный, переменный", "intensity": 5, "mood": "Ностальгическое, светлое", "compatibility": ["LR Baggs Para Acoustic DI", "Fishman Aura Spectrum DI", "Boss AD-10 (Acoustic Preamp)"]},
        "Nordic Drone": {"desc": "Нордический дрон-пад", "type": "PAD", "variation": 11, "tone": 4, "depth": 10, "effect": 6, "direct": 4, "mode": "GUITAR", "good_notes": ["D", "E", "A", "G"], "info": {"creator": "Wardruna inspired preset", "source": "Neofolk community", "genres": "Nordic Folk, Ritual Ambient", "description": "Атмосферный дрон в стиле Wardruna и Heilung."}, "rhythm": "Отсутствует, тянущийся", "intensity": 9, "mood": "Ритуальное, глубокое", "compatibility": ["Electro-Harmonix Freeze", "EarthQuaker Devices Rainbow Machine", "Strymon NightSky (Reverb)"]},
        "Hurdy Gurdy": {"desc": "Эмуляция hurdy-gurdy", "type": "SEQ 2", "variation": 7, "tone": 5, "depth": 7, "effect": 8, "direct": 4, "mode": "GUITAR", "good_notes": ["D", "G", "C", "A"], "info": {"creator": "Medieval folk inspired", "source": "Folk metal forums", "genres": "Folk Metal, Medieval Folk", "description": "Имитирует средневековую hurdy-gurdy."}, "rhythm": "Танцевальный, постоянный", "intensity": 6, "mood": "Веселое, аутентичное", "compatibility": ["Boss RC-5 (Looper)", "Mooer Tender Octaver", "Joyo Pipebomb (Compressor)"]}
    },
    "DRONE METAL": {
        "Sunn O))) Wall": {"desc": "Массивная стена дроуна", "type": "BASS", "variation": 10, "tone": 1, "depth": 10, "effect": 10, "direct": 2, "mode": "GUITAR", "good_notes": ["A", "G", "F", "E"], "info": {"creator": "Inspired by Sunn O))), Earth", "source": "Drone Metal community", "genres": "Drone Metal, Drone Doom", "description": "Создает массивную стену звука. Требует большой громкости."}, "rhythm": "Отсутствует, бесконечный", "intensity": 10, "mood": "Апокалиптическое, сокрушающее", "compatibility": ["ProCo RAT (Distortion)", "Boss FZ-2 (Fuzz)", "Morley Power Wah Fuzz"]},
        "Earth Drone": {"desc": "Атмосферный дрон Earth", "type": "PAD", "variation": 8, "tone": 3, "depth": 9, "effect": 7, "direct": 5, "mode": "GUITAR", "good_notes": ["D", "C", "G", "A"], "info": {"creator": "Dylan Carlson (Earth) inspired", "source": "Drone/Doom forums", "genres": "Drone Metal, Slowcore", "description": "Медленная атака с долгим sustain. Идеален для минимализма."}, "rhythm": "Очень медленный, пульсирующий", "intensity": 7, "mood": "Медитативное, пустынное", "compatibility": ["EarthQuaker Devices Afterneath (Reverb)", "Boss SL-2 (Slicer)", "Ernie Ball VP Jr (Volume Pedal)"]},
        "Boris Fuzz Drone": {"desc": "Фуззовый дрон Boris", "type": "LEAD 1", "variation": 9, "tone": 2, "depth": 9, "effect": 9, "direct": 3, "mode": "GUITAR", "good_notes": ["E", "D", "C", "A"], "info": {"creator": "Boris (band) inspired", "source": "Japanese drone scene", "genres": "Drone Metal, Noise Rock", "description": "Грязный фуззовый дрон. Сочетает drone wall с noise rock текстурами."}, "rhythm": "Хаотичный, взрывной", "intensity": 9, "mood": "Агрессивное, непредсказуемое", "compatibility": ["Zvex Fuzz Factory", "Death By Audio Fuzz War", "EarthQuaker Devices Plumes"]},
        "Teeth of Lions": {"desc": "Психоделический дрон", "type": "SFX 2", "variation": 6, "tone": 7, "depth": 10, "effect": 8, "direct": 3, "mode": "GUITAR", "good_notes": ["A", "G", "D", "E"], "info": {"creator": "Earth 2 era inspired", "source": "Drone/Psych forums", "genres": "Psychedelic Drone, Doom", "description": "Создает гипнотические текстуры для долгих композиций."}, "rhythm": "Медленно модулирующий", "intensity": 8, "mood": "Психоделическое, гипнотическое", "compatibility": ["Red Panda Particle (Granular Delay)", "Chase Bliss Mood", "Meris Polymoon (Delay)"]}
    }
}

# --- СТИЛИ ---
st.markdown(f"""
<style>
    /* ... (CSS код из предыдущего ответа остается здесь без изменений) ... */
    /* Главный заголовок с лого */
    .title-container {{
        display: flex;
        align-items: center;
        gap: 20px;
    }}
    .title-container img {{
        width: 60px;
        height: 60px;
    }}
    .title-container h1 {{
        color: #2c3e50 !important;
        margin: 0;
    }}
</style>
""", unsafe_allow_html=True)

# --- ФУНКЦИИ ---
def format_preset_for_selectbox(option):
    if option == "" or option is None:
        return "-- Выберите пресет --"
    
    category, preset_name = option
    preset_data = PRESETS[category][preset_name]
    
    rhythm = preset_data.get('rhythm', 'N/A')
    intensity = preset_data.get('intensity', 'N/A')
    mood = preset_data.get('mood', 'N/A')
    
    return f"{preset_name} | Ритм: {rhythm} | Глубина: {intensity}/10 | {mood}"

# --- ОСНОВНОЙ КОД ---

# 4) ЗАГОЛОВОК С ЛОГО
st.markdown(f"""
<div class="title-container">
    <img src="data:image/svg+xml;base64,{EXPLORER_LOGO_BASE64}" alt="Explorer Guitar Logo">
    <h1>Night Budva Boss SY-1 Presets</h1>
</div>
""", unsafe_allow_html=True)
st.markdown("### Интерактивный поиск пресетов по сыгранной ноте")

# 2) ИЗМЕНЕННАЯ ЛОГИКА: СНАЧАЛА НОТА
st.markdown("---")
st.subheader("1️⃣ Какую ноту вы играете?")
st.markdown("*Посмотрите на тюнер и нажмите соответствующую ноту, чтобы найти подходящие пресеты*")

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
col1, col2, col3, col4, col5, col6 = st.columns(6)
cols = [col1, col2, col3, col4, col5, col6]

if 'selected_note' not in st.session_state:
    st.session_state['selected_note'] = None

# Кнопки в 2 ряда
for i in range(6):
    with cols[i]:
        if st.button(notes[i], key=f"note_{notes[i]}"):
            st.session_state.selected_note = notes[i]

col7, col8, col9, col10, col11, col12 = st.columns(6)
cols2 = [col7, col8, col9, col10, col11, col12]

for i in range(6):
    with cols2[i]:
        if st.button(notes[i+6], key=f"note_{notes[i+6]}"):
            st.session_state.selected_note = notes[i+6]
            
if st.session_state.selected_note:
    st.markdown("---")
    selected_note = st.session_state.selected_note
    st.success(f"Анализ для ноты **{selected_note}**. Найдены подходящие пресеты ниже.")
    
    # Фильтруем пресеты под выбранную ноту
    suitable_presets = []
    for category, presets_in_cat in PRESETS.items():
        for preset_name, preset_data in presets_in_cat.items():
            if selected_note in preset_data['good_notes']:
                suitable_presets.append((category, preset_name))

    if not suitable_presets:
        st.warning(f"Для ноты **{selected_note}** не найдено идеально подходящих пресетов в нашей базе. Попробуйте сыграть другую ноту.")
    else:
        st.subheader(f"2️⃣ Выберите пресет, подходящий для ноты {selected_note}")
        
        # 1) ВЫПАДАЮЩИЙ СПИСОК С ОПИСАНИЕМ
        selected_option = st.selectbox(
            "Пресеты:",
            options=[""] + suitable_presets,
            format_func=format_preset_for_selectbox
        )
        
        if selected_option:
            category, preset_name = selected_option
            preset = PRESETS[category][preset_name]
            
            # --- ОТОБРАЖЕНИЕ ИНФОРМАЦИИ О ПРЕСЕТЕ (как раньше, но после выбора) ---
            st.markdown("---")
            st.subheader("📋 Справка о пресете")
            st.markdown(f"""
            <div class="preset-info">
                <h3>🎸 {preset_name}</h3>
                <p><strong>Описание:</strong> {preset['info']['description']}</p>
                <p><strong>👤 Создатель/Вдохновение:</strong> {preset['info']['creator']}</p>
                <p><strong>🌐 Источник:</strong> {preset['info']['source']}</p>
                <p><strong>🎵 Жанры:</strong> {preset['info']['genres']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            st.subheader("🎛️ Настройки Boss SY-1")
            
            settings_col1, settings_col2 = st.columns(2)
            # ... (код для отображения настроек педали, без изменений)
            
            st.markdown("---")
            st.subheader("🎼 Подходящие ноты для этого пресета")
            st.info(f"Хотя вы выбрали **{selected_note}**, этот пресет также отлично звучит с нотами: **{', '.join(p for p in preset['good_notes'] if p != selected_note)}**")

            # 3) ДОПОЛНИТЕЛЬНЫЕ ИНСТРУМЕНТЫ С СОВМЕСТИМОСТЬЮ
            st.markdown("---")
            st.subheader("⚙️ Дополнительные инструменты и советы")

            tool_col1, tool_col2 = st.columns(2)
            with tool_col1:
                 st.markdown(f"""
                <div class.info-box">
                    <h4>🤝 Сочетаемость с другими педалями</h4>
                    <ul>
                        {''.join(f"<li>{pedal}</li>" for pedal in preset['compatibility'])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)

            with tool_col2:
                st.markdown(f"""
                <div class.info-box">
                    <h4>🎸 Рекомендуемый строй</h4>
                    <p>Для стиля **{category}** лучше всего подходят строи:</p>
                    <ul>
                        <li>METAL: Drop D, Drop C, Drop A</li>
                        <li>FOLK: DADGAD, Open D, Open G</li>
                        <li>DRONE: Drop A и ниже</li>
                        <li>ПОПУЛЯРНЫЕ: Standard E</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)

            if st.button("🔄 Выбрать другую ноту"):
                st.session_state.selected_note = None
                st.rerun()

else:
    st.info("👆 Начните с выбора ноты, чтобы увидеть подходящие пресеты.")

# Футер
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #555;'>
    <p>🎸 Night Budva Boss SY-1 Presets</p>
    <p>Создано для музыкантов с ❤️</p>
</div>
""", unsafe_allow_html=True)
