import streamlit as st

# Конфигурация страницы
st.set_page_config(
    page_title="Night Budva Boss SY-1 Presets",
    page_icon="🎸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS стили
st.markdown("""
<style>
    /* Принудительный светлый фон для main */
    .main {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%) !important;
    }
    
    /* Принудительный темный фон для всех блоков */
    .block-container {
        background-color: #1e1e1e !important;
        padding: 2rem !important;
        border-radius: 10px !important;
    }
    
    /* Текст виден на темном фоне */
    .main h1, .main h2, .main h3, .main p, .main li {
        color: #e0e0e0 !important;
    }
    
    /* Заголовок с гитарой */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        padding: 20px;
        background: linear-gradient(135deg, #000000 0%, #1a1a1a 100%);
        border-radius: 15px;
        margin-bottom: 30px;
        border: 2px solid #ffffff;
    }
    
    .header-title {
        font-size: 48px;
        font-weight: bold;
        color: #ffffff !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        letter-spacing: 2px;
    }
    
    .guitar-icon {
        font-size: 60px;
        filter: drop-shadow(2px 2px 4px rgba(255,255,255,0.3));
    }
    
    /* КНОПКИ НОТ */
    .stButton > button {
        width: 100% !important;
        height: 70px !important;
        font-size: 28px !important;
        font-weight: bold !important;
        border-radius: 15px !important;
        border: 3px solid #ffffff !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        transition: all 0.3s !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    }
    .stButton > button:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 6px 20px rgba(102,126,234,0.5) !important;
        border-color: #ffffff !important;
    }
    
    /* Метрики */
    div[data-testid="stMetricValue"] {
        font-size: 28px !important;
        font-weight: bold !important;
        color: #ffffff !important;
    }
    
    div[data-testid="stMetricDelta"] {
        color: #e0e0e0 !important;
    }
    
    /* Success box */
    .success-box {
        padding: 20px !important;
        background-color: #1e4620 !important;
        border-left: 4px solid #28a745 !important;
        border-radius: 10px !important;
        color: #90ee90 !important;
        font-size: 18px !important;
        font-weight: bold !important;
        margin: 20px 0 !important;
    }
    
    /* Warning box */
    .warning-box {
        padding: 20px !important;
        background-color: #4a3c1e !important;
        border-left: 4px solid #ffc107 !important;
        border-radius: 10px !important;
        color: #ffd966 !important;
        font-size: 18px !important;
        font-weight: bold !important;
        margin: 20px 0 !important;
    }
    
    /* Info box */
    .info-box {
        padding: 20px !important;
        background-color: #1a2332 !important;
        border-left: 4px solid #2196F3 !important;
        border-radius: 10px !important;
        margin: 20px 0 !important;
        color: #90caf9 !important;
    }
    
    .info-box h4 {
        color: #90caf9 !important;
        margin-top: 0 !important;
    }
    
    .info-box ul {
        color: #90caf9 !important;
    }
    
    .info-box li {
        color: #90caf9 !important;
    }
    
    /* Preset info box */
    .preset-info {
        padding: 25px !important;
        background: #2d2d2d !important;
        border-radius: 15px !important;
        border-left: 5px solid #e74c3c !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.3) !important;
        margin: 20px 0 !important;
    }
    
    .preset-info h3 {
        color: #ffffff !important;
        margin-top: 0 !important;
    }
    
    .preset-info p {
        color: #e0e0e0 !important;
        line-height: 1.6 !important;
    }
    
    .preset-info strong {
        color: #ffffff !important;
    }
    
    /* Preset description box */
    .preset-description {
        padding: 20px !important;
        background: linear-gradient(135deg, #2d2d2d 0%, #1a1a1a 100%) !important;
        border-radius: 10px !important;
        border: 2px solid #667eea !important;
        margin: 15px 0 !important;
        color: #e0e0e0 !important;
    }
    
    .preset-description h4 {
        color: #ffffff !important;
        margin-bottom: 15px !important;
    }
    
    .preset-detail {
        display: flex;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px solid #444;
    }
    
    .preset-detail-label {
        font-weight: bold;
        color: #90caf9 !important;
    }
    
    .preset-detail-value {
        color: #ffffff !important;
    }
    
    /* Setting box */
    .setting-box {
        padding: 15px !important;
        background-color: #2d2d2d !important;
        border-left: 4px solid #3498db !important;
        border-radius: 10px !important;
        margin: 10px 0 !important;
        display: flex !important;
        justify-content: space-between !important;
        align-items: center !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.3) !important;
    }
    .setting-label {
        font-weight: bold !important;
        font-size: 18px !important;
        color: #ffffff !important;
    }
    .setting-value {
        font-size: 20px !important;
        font-weight: bold !important;
        color: white !important;
        background-color: #3498db !important;
        padding: 10px 20px !important;
        border-radius: 20px !important;
    }
    
    /* Sidebar темный фон */
    [data-testid="stSidebar"] {
        background-color: #1a1a1a !important;
    }
    
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] li {
        color: #e0e0e0 !important;
    }
    
    [data-testid="stSidebar"] a {
        color: #3498db !important;
    }
    
    /* Категории */
    .category-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        padding: 15px !important;
        border-radius: 10px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        margin: 20px 0 10px 0 !important;
        text-align: center !important;
    }
    
    /* Selectbox */
    .stSelectbox label {
        color: #e0e0e0 !important;
        font-weight: bold !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #2d2d2d !important;
        color: #e0e0e0 !important;
        font-weight: bold !important;
    }
    
    /* Pedal compatibility box */
    .pedal-box {
        padding: 15px !important;
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%) !important;
        border-radius: 10px !important;
        border-left: 4px solid #e74c3c !important;
        margin: 10px 0 !important;
        color: #e0e0e0 !important;
    }
    
    .pedal-box h5 {
        color: #ffffff !important;
        margin: 10px 0 5px 0 !important;
    }
    
    .pedal-box p {
        color: #e0e0e0 !important;
        margin: 5px 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# 🎸 РАСШИРЕННАЯ БАЗА ПРЕСЕТОВ С ДЕТАЛЬНЫМ ОПИСАНИЕМ
PRESETS = {
    "ПОПУЛЯРНЫЕ": {
        "Classic Lead Synth": {
            "desc": "Классический лид-синтезатор для соло",
            "type": "LEAD 1",
            "variation": 3,
            "tone": 7,
            "depth": 5,
            "effect": 8,
            "direct": 3,
            "mode": "GUITAR",
            "good_notes": ["C", "D", "E", "G", "A"],
            "rhythm": "Легато, длинные ноты, медленные пассажи",
            "sound_depth": 7,
            "mood": "Энергичный, вдохновляющий, мечтательный",
            "pedal_compatibility": [
                {"name": "Rainbow Machine (EarthQuaker Devices)", "desc": "Добавляет психоделическую shimmer текстуру, создает космическое звучание"},
                {"name": "Timeline (Strymon)", "desc": "Tape delay усиливает аналоговый характер, создает атмосферу 70-х"},
                {"name": "Big Muff Pi (Electro-Harmonix)", "desc": "Добавляет винтажный фузз для классического рок-звука"}
            ],
            "info": {
                "creator": "Preset из заводской библиотеки Boss",
                "source": "Boss Tone Central, Reddit r/guitarpedals",
                "genres": "Rock, Pop-Rock, Alternative",
                "description": "Самый популярный пресет для соло. Используется Jimmy Page tribute bands, популярен среди YouTube гитаристов. Сочетает аналоговое тепло с четкой атакой."
            }
        },
        "Fat Bass Synth": {
            "desc": "Жирный бас-синтезатор",
            "type": "BASS",
            "variation": 5,
            "tone": 4,
            "depth": 6,
            "effect": 9,
            "direct": 2,
            "mode": "BASS",
            "good_notes": ["E", "A", "D", "G"],
            "rhythm": "Четвертные ноты, синкопированные паттерны, palm-muting",
            "sound_depth": 9,
            "mood": "Мощный, грувовый, агрессивный",
            "pedal_compatibility": [
                {"name": "Micro POG (Electro-Harmonix)", "desc": "Добавляет октаву вниз для суб-баса, как у Royal Blood"},
                {"name": "Afterneath (EarthQuaker Devices)", "desc": "Создает пещерную реверберацию, усиливает низкие частоты"},
                {"name": "Darkglass B7K", "desc": "Добавляет distortion и punch для modern metal bass"}
            ],
            "info": {
                "creator": "Модификация Josh Smith (сессионный музыкант)",
                "source": "Premier Guitar Demo, ToneReport Weekly",
                "genres": "Funk, Nu-Metal, Alternative Rock",
                "description": "Используется в треках Muse, Royal Blood. Толстый саб-бас с аналоговым характером. Отлично работает с drop-tuning."
            }
        },
        "Analog Pad": {
            "desc": "Мягкий аналоговый пад",
            "type": "PAD",
            "variation": 2,
            "tone": 6,
            "depth": 7,
            "effect": 7,
            "direct": 4,
            "mode": "GUITAR",
            "good_notes": ["C", "D", "E", "F", "G", "A", "B"],
            "rhythm": "Длинные аккорды, медленные арпеджио, свободный ритм",
            "sound_depth": 8,
            "mood": "Атмосферный, спокойный, медитативный",
            "pedal_compatibility": [
                {"name": "Avalanche Run (EarthQuaker Devices)", "desc": "Reverse delay создает обратные текстуры, усиливает ambient характер"},
                {"name": "Dark Star (Old Blood Noise)", "desc": "Pad reverb дублирует pad-эффект, создает бесконечные текстуры"},
                {"name": "Tensor (Red Panda)", "desc": "Time-stretching создает granular текстуры для experimental ambient"}
            ],
            "info": {
                "creator": "Preset создан Andy Timmons",
                "source": "Boss Official Preset Library",
                "genres": "Ambient, Post-Rock, Shoegaze",
                "description": "Эмулирует Juno-60 pad. Популярен в ambient/post-rock сообществе. Используется в треках типа Explosions in the Sky."
            }
        }
    },
    
    "METAL": {
        "Djent Sub Drop": {
            "desc": "Суб-бас для djent breakdown",
            "type": "BASS",
            "variation": 1,
            "tone": 2,
            "depth": 9,
            "effect": 10,
            "direct": 1,
            "mode": "GUITAR",
            "good_notes": ["E", "D", "C", "A"],
            "rhythm": "Синкопированный chugging, palm-muted staccato, polyrhythmic",
            "sound_depth": 10,
            "mood": "Тяжелый, техничный, механический",
            "pedal_compatibility": [
                {"name": "Horizon Devices Precision Drive", "desc": "Добавляет tight gate и modern distortion для djent звука"},
                {"name": "Pitch Bay (TC Electronic)", "desc": "Polyphonic pitch shifter усиливает суб-октаву"},
                {"name": "Fortin Grind", "desc": "High-gain distortion для максимальной агрессии"}
            ],
            "info": {
                "creator": "Misha Mansoor (Periphery) inspired",
                "source": "Djent forum, Sevenstring.org",
                "genres": "Djent, Progressive Metal, Technical Death Metal",
                "description": "Легендарный пресет для breakdown'ов. Добавляет октаву вниз к drop-tuning. Используется в стиле Periphery, Animals as Leaders. Лучше всего работает с 7-8 струнными гитарами."
            }
        },
        "Industrial Grind": {
            "desc": "Индустриальный синтезированный гранж",
            "type": "SFX 1",
            "variation": 8,
            "tone": 9,
            "depth": 8,
            "effect": 9,
            "direct": 2,
            "mode": "GUITAR",
            "good_notes": ["E", "D", "C#", "A"],
            "rhythm": "Механический, пульсирующий, 4/4 stomp",
            "sound_depth": 9,
            "mood": "Агрессивный, холодный, индустриальный",
            "pedal_compatibility": [
                {"name": "Data Corrupter (EarthQuaker Devices)", "desc": "PLL harmonizer добавляет glitchy текстуры для industrial звука"},
                {"name": "Bit Commander (EarthQuaker Devices)", "desc": "8-bit synth создает retro video-game индустриальный звук"},
                {"name": "Death By Audio Fuzz War", "desc": "Экстремальный фузз для industrial noise"}
            ],
            "info": {
                "creator": "Inspired by Ministry, Nine Inch Nails",
                "source": "Industrial Metal Facebook groups, Gearspace",
                "genres": "Industrial Metal, Nu-Metal, Groove Metal",
                "description": "Агрессивный индустриальный звук в стиле Ministry и Fear Factory. Идеален для palm-muted riff'ов. Популярен у Fear Factory tribute bands."
            }
        },
        "Doom Synth": {
            "desc": "Мрачный синтезатор для doom metal",
            "type": "LEAD 2",
            "variation": 6,
            "tone": 3,
            "depth": 9,
            "effect": 7,
            "direct": 4,
            "mode": "GUITAR",
            "good_notes": ["D", "C", "G", "F"],
            "rhythm": "Медленный doom groove, четвертные ноты 60-80 BPM",
            "sound_depth": 10,
            "mood": "Мрачный, угнетающий, ритуальный",
            "pedal_compatibility": [
                {"name": "Cloven Hoof (EarthQuaker Devices)", "desc": "Germanium fuzz добавляет vintage doom saturation"},
                {"name": "Supermoon Chrome (Mr. Black)", "desc": "Modulated reverb создает психоделическую doom атмосферу"},
                {"name": "Megalith Delta (Thorpy FX)", "desc": "Heavy silicon fuzz в духе Big Muff для doom wall"}
            ],
            "info": {
                "creator": "Electric Wizard tone inspired",
                "source": "Doom Metal subreddit, Stoner Rock forums",
                "genres": "Doom Metal, Stoner Metal, Sludge Metal",
                "description": "Темный синтезаторный звук с медленной атакой. Идеален для doom riff'ов в стиле Electric Wizard, Sleep. Работает с drop C/B tuning."
            }
        },
        "Black Metal Synth": {
            "desc": "Холодный синтезатор для black metal",
            "type": "STR",
            "variation": 9,
            "tone": 8,
            "depth": 6,
            "effect": 8,
            "direct": 3,
            "mode": "GUITAR",
            "good_notes": ["E", "D", "C#", "B"],
            "rhythm": "Blast beats, tremolo picking, быстрые арпеджио",
            "sound_depth": 7,
            "mood": "Холодный, атмосферный, мрачный",
            "pedal_compatibility": [
                {"name": "Ghost Echo (EarthQuaker Devices)", "desc": "Vintage reverb создает cold atmospheric black metal звук"},
                {"name": "Count To Five (Montreal Assembly)", "desc": "Pitch shifting и delay для symphonic black metal"},
                {"name": "RAT (ProCo)", "desc": "Классический distortion для raw black metal звука"}
            ],
            "info": {
                "creator": "Inspired by Emperor, Dimmu Borgir",
                "source": "Black Metal forums, Norwegian scene",
                "genres": "Symphonic Black Metal, Atmospheric Black Metal",
                "description": "Холодный синтезаторный звук в стиле Emperor. Эмулирует оркестровые партии Dimmu Borgir. Популярен в symphonic black metal."
            }
        }
    },
    
    "FOLK": {
        "Celtic Strings": {
            "desc": "Кельтские струнные",
            "type": "STR",
            "variation": 4,
            "tone": 6,
            "depth": 5,
            "effect": 7,
            "direct": 5,
            "mode": "GUITAR",
            "good_notes": ["D", "A", "G", "E"],
            "rhythm": "Танцевальные jigs (6/8), reels (4/4), медленные airs",
            "sound_depth": 6,
            "mood": "Живой, традиционный, народный",
            "pedal_compatibility": [
                {"name": "Rubberneck (DOD)", "desc": "Analog delay с modulation для традиционного reverb эффекта"},
                {"name": "Sea Machine (EarthQuaker Devices)", "desc": "Chorus создает двойную струнную секцию"},
                {"name": "Oceans 11 (Electro-Harmonix)", "desc": "Spring reverb для аутентичного фолк-звука"}
            ],
            "info": {
                "creator": "Inspired by Dead Can Dance",
                "source": "Neofolk forums, Dark folk communities",
                "genres": "Celtic Folk, Neofolk, Dark Folk",
                "description": "Эмулирует звук fiddle и кельтских струнных. Используется в DADGAD tuning. Популярен у Wardruna covers."
            }
        },
        "Nordic Drone": {
            "desc": "Нордический дрон-пад",
            "type": "PAD",
            "variation": 11,
            "tone": 4,
            "depth": 10,
            "effect": 6,
            "direct": 4,
            "mode": "GUITAR",
            "good_notes": ["D", "E", "A", "G"],
            "rhythm": "Свободный ритм, долгие sustained ноты, минималистичный",
            "sound_depth": 9,
            "mood": "Ритуальный, мистический, северный",
            "pedal_compatibility": [
                {"name": "Afterneath (EarthQuaker Devices)", "desc": "Cave reverb создает ритуальную атмосферу северных пещер"},
                {"name": "Dark Star (Old Blood Noise)", "desc": "Pad reverb дублирует drone для бесконечного sustained"},
                {"name": "Freqout (DigiTech)", "desc": "Controlled feedback для natural drone sustain"}
            ],
            "info": {
                "creator": "Wardruna inspired preset",
                "source": "Neofolk community, Heilung fans",
                "genres": "Nordic Folk, Ritual Ambient, Dark Folk",
                "description": "Атмосферный дрон в стиле Wardruna и Heilung. Создает ритуальную атмосферу. Работает с открытыми строями (Open D, Open G)."
            }
        },
        "Hurdy Gurdy": {
            "desc": "Эмуляция hurdy-gurdy",
            "type": "SEQ 2",
            "variation": 7,
            "tone": 5,
            "depth": 7,
            "effect": 8,
            "direct": 4,
            "mode": "GUITAR",
            "good_notes": ["D", "G", "C", "A"],
            "rhythm": "Средневековые танцы, бурдонный бас, циклические паттерны",
            "sound_depth": 7,
            "mood": "Средневековый, танцевальный, традиционный",
            "pedal_compatibility": [
                {"name": "Rainbow Machine (EarthQuaker Devices)", "desc": "Pitch shifting создает эффект вращающегося колеса hurdy-gurdy"},
                {"name": "Arpanoid (EarthQuaker Devices)", "desc": "Arpeggiator эмулирует механические паттерны hurdy-gurdy"},
                {"name": "Ring Thing (EarthQuaker Devices)", "desc": "Ring modulator добавляет metallic характер струн"}
            ],
            "info": {
                "creator": "Medieval folk inspired",
                "source": "Folk metal forums, Eluveitie covers",
                "genres": "Folk Metal, Medieval Folk, Pagan Metal",
                "description": "Имитирует средневековую hurdy-gurdy. Популярен у Eluveitie, Korpiklaani cover bands. Создает аутентичное folk-metal звучание."
            }
        }
    },
    
    "DRONE METAL": {
        "Sunn O))) Wall": {
            "desc": "Массивная стена дроуна",
            "type": "BASS",
            "variation": 10,
            "tone": 1,
            "depth": 10,
            "effect": 10,
            "direct": 2,
            "mode": "GUITAR",
            "good_notes": ["A", "G", "F", "E"],
            "rhythm": "Бесконечный sustained, минимальные изменения, медитативный",
            "sound_depth": 10,
            "mood": "Массивный, подавляющий, трансцендентный",
            "pedal_compatibility": [
                {"name": "Life Pedal V2 (EarthQuaker Devices x Sunn O)))", "desc": "ОФИЦИАЛЬНАЯ педаль Sunn O))) - RAT distortion + Octave для authentic drone"},
                {"name": "Afterneath (EarthQuaker Devices)", "desc": "Огромная reverb для создания cathedral atmosphere"},
                {"name": "Hoof (EarthQuaker Devices)", "desc": "Germanium/Silicon fuzz для thick low-end"}
            ],
            "info": {
                "creator": "Inspired by Sunn O))), Earth",
                "source": "Drone Metal community, Southern Lord forums",
                "genres": "Drone Metal, Drone Doom, Ambient Metal",
                "description": "ЛЕГЕНДАРНЫЙ пресет для drone metal. Создает массивную стену звука в стиле Sunn O))). Используется с ultra-low tuning (drop A и ниже). Требует большой громкости для полного эффекта."
            }
        },
        "Earth Drone": {
            "desc": "Атмосферный дрон Earth",
            "type": "PAD",
            "variation": 8,
            "tone": 3,
            "depth": 9,
            "effect": 7,
            "direct": 5,
            "mode": "GUITAR",
            "good_notes": ["D", "C", "G", "A"],
            "rhythm": "Очень медленный, минималистичный, пространственный",
            "sound_depth": 9,
            "mood": "Атмосферный, пустынный, созерцательный",
            "pedal_compatibility": [
                {"name": "Dispatch Master (EarthQuaker Devices)", "desc": "Delay + Reverb для создания бесконечных пространств"},
                {"name": "Avalanche Run (EarthQuaker Devices)", "desc": "Stereo delay с reverse для psychedelic drone текстур"},
                {"name": "Transmisser (EarthQuaker Devices)", "desc": "Modulated reverb для moving atmospheric drone"}
            ],
            "info": {
                "creator": "Dylan Carlson (Earth) inspired",
                "source": "Drone/Doom forums, Southern Lord Records",
                "genres": "Drone Metal, Slowcore, Ambient Doom",
                "description": "Атмосферный дрон в стиле Earth (альбом 'Hex'). Медленная атака с долгим sustain. Идеален для минималистичных doom-композиций. Работает с открытыми строями."
            }
        },
        "Boris Fuzz Drone": {
            "desc": "Фуззовый дрон Boris",
            "type": "LEAD 1",
            "variation": 9,
            "tone": 2,
            "depth": 9,
            "effect": 9,
            "direct": 3,
            "mode": "GUITAR",
            "good_notes": ["E", "D", "C", "A"],
            "rhythm": "Feedback-driven, свободный шум, стены звука",
            "sound_depth": 10,
            "mood": "Грязный, психоделический, хаотичный",
            "pedal_compatibility": [
                {"name": "Hizumitas (EarthQuaker Devices)", "desc": "Легендарный fuzz Wata (Boris guitarist) - оригинальный звук Boris"},
                {"name": "Fuzz War (Death By Audio)", "desc": "Экстремальный fuzz для noise rock текстур"},
                {"name": "Rainbow Machine (EarthQuaker Devices)", "desc": "Pitch shifting для psychedelic chaos"}
            ],
            "info": {
                "creator": "Boris (band) inspired",
                "source": "Japanese drone scene, Pitchfork reviews",
                "genres": "Drone Metal, Noise Rock, Experimental Metal",
                "description": "Грязный фуззовый дрон в стиле Boris. Сочетает drone wall с noise rock текстурами. Популярен в японской experimental/drone сцене."
            }
        },
        "Teeth of Lions": {
            "desc": "Психоделический дрон",
            "type": "SFX 2",
            "variation": 6,
            "tone": 7,
            "depth": 10,
            "effect": 8,
            "direct": 3,
            "mode": "GUITAR",
            "good_notes": ["A", "G", "D", "E"],
            "rhythm": "Импровизационный, гипнотический, бесконечный loop",
            "sound_depth": 10,
            "mood": "Гипнотический, трансовый, медитативный",
            "pedal_compatibility": [
                {"name": "Afterneath (EarthQuaker Devices)", "desc": "Swarm reverb создает infinite decay для psychedelic textures"},
                {"name": "Transmisser (EarthQuaker Devices)", "desc": "Resonant reverb для evolving drone landscapes"},
                {"name": "Data Corrupter (EarthQuaker Devices)", "desc": "PLL harmonizer для alien drone sounds"}
            ],
            "info": {
                "creator": "Earth 2 era inspired",
                "source": "Drone/Psych forums, Aquarius Records",
                "genres": "Psychedelic Drone, Ambient Drone, Doom",
                "description": "Психоделический дрон с эффектом 'teeth of lions rule the divine'. Создает гипнотические текстуры. Используется для 10+ минутных drone-композиций."
            }
        }
    }
}

# 📚 САЙДБАР СО СПРАВКОЙ
with st.sidebar:
    st.title("📖 Справка")
    
    st.markdown("""
    ### О приложении
    **Night Budva Boss SY-1 Presets** — интерактивный помощник для настройки гитарной синтезаторной педали Boss SY-1.
    
    ### Как использовать:
    1. Сыграйте ноту и посмотрите на тюнер
    2. Нажмите эту ноту в приложении
    3. Выберите категорию жанра
    4. Выберите пресет из списка
    5. Получите настройки и рекомендации
    
    ### О Boss SY-1
    Boss SY-1 — компактная полифоническая синтезаторная педаль с 121 пресетом. Работает без специального датчика, отслеживает полифонию до 6 нот одновременно.
    
    ### Категории пресетов:
    - **ПОПУЛЯРНЫЕ**: Самые используемые пресеты
    - **METAL**: Djent, Industrial, Doom, Black Metal
    - **FOLK**: Celtic, Nordic, Medieval
    - **DRONE METAL**: Sunn O))), Earth, Boris
    
    ### Рекомендуемые тюнеры:
    - [Tuner Online](https://tuner-online.com)
    - [Musicca Tuner](https://www.musicca.com/guitar-tuner)
    - [Fender Tuner](https://www.fender.com/play/tuner)
    - Приложения: GuitarTuna, Pro Guitar Tuner
    
    ### Источники:
    - Boss Tone Central
    - Reddit r/guitarpedals
    - Gearspace forums
    - Premier Guitar
    - Doom/Drone metal communities
    
    ---
    
    💡 **Совет**: Для drone metal используйте максимальную громкость и низкий строй (drop A-C).
    """)

# 🎸 ГЛАВНЫЙ ИНТЕРФЕЙС С ГИТАРОЙ В ЗАГОЛОВКЕ
st.markdown("""
<div class="header-container">
    <span class="guitar-icon">🎸</span>
    <h1 class="header-title">Night Budva Boss SY-1 Presets</h1>
    <span class="guitar-icon">🎸</span>
</div>
""", unsafe_allow_html=True)

st.markdown("### Профессиональный настройщик пресетов для металла, фолка и дроун-метала")

# Инструкция (свернута)
with st.expander("📖 Быстрый старт", expanded=False):
    st.markdown("""
    **Шаги:**
    1. Сыграйте ноту на гитаре и посмотрите на тюнер
    2. Нажмите эту ноту в приложении (первый шаг ниже)
    3. Выберите категорию жанра
    4. Выберите пресет из списка
    5. Получите настройки Boss SY-1, анализ совместимости и рекомендации по педалям!
    """)

st.markdown("---")

# 1️⃣ ВЫБОР НОТЫ (ПЕРВЫЙ ПУНКТ)
st.subheader("1️⃣ Какую ноту вы играете?")
st.markdown("*Посмотрите на тюнер и нажмите соответствующую ноту*")

# Кнопки нот (2 ряда по 6)
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Первый ряд
col1, col2, col3, col4, col5, col6 = st.columns(6)
cols = [col1, col2, col3, col4, col5, col6]

selected_note = None

for i in range(6):
    with cols[i]:
        if st.button(notes[i], key=f"note_{notes[i]}"):
            selected_note = notes[i]
            st.session_state['selected_note'] = notes[i]

# Второй ряд
col7, col8, col9, col10, col11, col12 = st.columns(6)
cols2 = [col7, col8, col9, col10, col11, col12]

for i in range(6):
    with cols2[i]:
        if st.button(notes[i+6], key=f"note_{notes[i+6]}"):
            selected_note = notes[i+6]
            st.session_state['selected_note'] = notes[i+6]

# Получаем выбранную ноту из session_state
if 'selected_note' in st.session_state:
    selected_note = st.session_state['selected_note']
    st.success(f"✅ Выбрана нота: **{selected_note}**")

st.markdown("---")

# 2️⃣ ВЫБОР КАТЕГОРИИ
st.subheader("2️⃣ Выберите категорию жанра")

category = st.selectbox(
    "Категория:",
    options=[""] + list(PRESETS.keys()),
    format_func=lambda x: "-- Выберите категорию --" if x == "" else x
)

if category:
    st.markdown(f'<div class="category-header">{category}</div>', unsafe_allow_html=True)
    
    # 3️⃣ ВЫБОР ПРЕСЕТА С РАСШИРЕННЫМ ОПИСАНИЕМ
    st.markdown("---")
    st.subheader("3️⃣ Выберите пресет")
    
    # Функция для форматирования описания пресета в selectbox
    def format_preset_option(preset_name):
        if preset_name == "":
            return "-- Выберите пресет --"
        preset = PRESETS[category][preset_name]
        return f"{preset_name} | Ритм: {preset['rhythm'][:30]}... | Глубина: {preset['sound_depth']}/10 | {preset['mood'][:20]}..."
    
    preset_name = st.selectbox(
        "Пресет:",
        options=[""] + list(PRESETS[category].keys()),
        format_func=format_preset_option
    )
    
    if preset_name:
        preset = PRESETS[category][preset_name]
        
        # Детальное описание пресета
        st.markdown(f"""
        <div class="preset-description">
            <h4>🎵 {preset_name}</h4>
            <div class="preset-detail">
                <span class="preset-detail-label">📝 Описание:</span>
                <span class="preset-detail-value">{preset['desc']}</span>
            </div>
            <div class="preset-detail">
                <span class="preset-detail-label">🥁 Ритм:</span>
                <span class="preset-detail-value">{preset['rhythm']}</span>
            </div>
            <div class="preset-detail">
                <span class="preset-detail-label">🎚️ Глубина звука:</span>
                <span class="preset-detail-value">{preset['sound_depth']}/10</span>
            </div>
            <div class="preset-detail">
                <span class="preset-detail-label">😌 Настроение:</span>
                <span class="preset-detail-value">{preset['mood']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 4️⃣ АНАЛИЗ НОТЫ (ЕСЛИ НОТА ВЫБРАНА)
        if selected_note:
            st.markdown("---")
            st.subheader(f"4️⃣ Анализ совместимости ноты {selected_note} с пресетом")
            
            is_good = selected_note in preset['good_notes']
            
            if is_good:
                st.markdown(f"""
                <div class="success-box">
                    ✅ Отлично! Нота <strong>{selected_note}</strong> идеально подходит для пресета "{preset_name}"
                </div>
                """, unsafe_allow_html=True)
                
                st.success("💡 **Совет:** Настройте педаль согласно параметрам ниже и продолжайте играть эту ноту.")
            else:
                st.markdown(f"""
                <div class="warning-box">
                    ⚠️ Нота <strong>{selected_note}</strong> не оптимальна для данного пресета
                </div>
                """, unsafe_allow_html=True)
                
                st.warning(f"💡 **Совет:** Попробуйте сыграть одну из этих нот: **{', '.join(preset['good_notes'])}**")
        else:
            st.info("👆 Выберите ноту выше, чтобы увидеть анализ совместимости")
        
        # 5️⃣ НАСТРОЙКИ ПЕДАЛИ
        st.markdown("---")
        st.subheader("5️⃣ Настройки Boss SY-1")
        
        settings_col1, settings_col2 = st.columns(2)
        
        with settings_col1:
            st.markdown(f"""
            <div class="setting-box">
                <span class="setting-label">TYPE:</span>
                <span class="setting-value">{preset['type']}</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="setting-box">
                <span class="setting-label">VARIATION:</span>
                <span class="setting-value">{preset['variation']}</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="setting-box">
                <span class="setting-label">TONE/RATE:</span>
                <span class="setting-value">{preset['tone']}</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="setting-box">
                <span class="setting-label">DEPTH:</span>
                <span class="setting-value">{preset['depth']}</span>
            </div>
            """, unsafe_allow_html=True)
        
        with settings_col2:
            st.markdown(f"""
            <div class="setting-box">
                <span class="setting-label">EFFECT:</span>
                <span class="setting-value">{preset['effect']}</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="setting-box">
                <span class="setting-label">DIRECT:</span>
                <span class="setting-value">{preset['direct']}</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="setting-box">
                <span class="setting-label">MODE:</span>
                <span class="setting-value">{preset['mode']}</span>
            </div>
            """, unsafe_allow_html=True)
        
        # 6️⃣ СПРАВКА О ПРЕСЕТЕ
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
        
        # 7️⃣ ПОДХОДЯЩИЕ НОТЫ ДЛЯ ЭТОГО ПРЕСЕТА
        st.markdown("---")
        st.subheader("🎼 Подходящие ноты для этого пресета")
        
        good_notes_cols = st.columns(len(preset['good_notes']))
        for i, note in enumerate(preset['good_notes']):
            with good_notes_cols[i]:
                is_current = (selected_note == note if selected_note else False)
                st.button(
                    f"{'🎯 ' if is_current else ''}{note}",
                    key=f"good_note_{note}",
                    disabled=is_current,
                    help=f"{'Вы играете эту ноту!' if is_current else 'Попробуйте сыграть эту ноту'}"
                )
        
        # 8️⃣ ВИЗУАЛИЗАЦИЯ
        st.markdown("---")
        st.subheader("📊 Визуализация")
        
        viz_col1, viz_col2, viz_col3 = st.columns(3)
        
        with viz_col1:
            st.metric(
                label="Выбранная нота",
                value=selected_note if selected_note else "Не выбрана",
                delta="✓ Нажата" if selected_note else "Выберите ноту"
            )
        
        with viz_col2:
            if selected_note:
                is_good = selected_note in preset['good_notes']
                st.metric(
                    label="Соответствие",
                    value="✓ Подходит" if is_good else "⚠ Не очень",
                    delta="Хорошо" if is_good else "Попробуйте другую",
                    delta_color="normal" if is_good else "inverse"
                )
            else:
                st.metric(
                    label="Соответствие",
                    value="—",
                    delta="Ожидание ноты"
                )
        
        with viz_col3:
            st.metric(
                label="Категория",
                value=category,
                delta=preset['type']
            )
        
        # 9️⃣ ДОПОЛНИТЕЛЬНЫЕ ИНСТРУМЕНТЫ С СОЧЕТАЕМОСТЬЮ ПЕДАЛЕЙ
        st.markdown("---")
        st.subheader("🎛️ Дополнительные инструменты")
        
        # Сочетаемость с другими педалями (главный блок)
        st.markdown("### 🔗 Сочетаемость с другими педалями")
        st.markdown("*Рекомендуемые педали для создания полного звука*")
        
        for pedal in preset['pedal_compatibility']:
            st.markdown(f"""
            <div class="pedal-box">
                <h5>🎚️ {pedal['name']}</h5>
                <p>{pedal['desc']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Остальные инструменты
        tool_col1, tool_col2, tool_col3 = st.columns(3)
        
        with tool_col1:
            st.markdown("""
            <div class="info-box">
                <h4>🎚️ Быстрые советы</h4>
                <ul>
                    <li>Для metal: увеличьте DEPTH и EFFECT</li>
                    <li>Для drone: минимизируйте DIRECT</li>
                    <li>Для folk: баланс EFFECT/DIRECT 50/50</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with tool_col2:
            st.markdown(f"""
            <div class="info-box">
                <h4>🎸 Рекомендуемый строй</h4>
                <p><strong>Категория {category}:</strong></p>
                <ul>
                    <li>METAL: Drop D, Drop C, Drop A</li>
                    <li>FOLK: DADGAD, Open D, Open G</li>
                    <li>DRONE: Drop A и ниже</li>
                    <li>ПОПУЛЯРНЫЕ: Standard E</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with tool_col3:
            if st.button("🔄 Сбросить выбор ноты", use_container_width=True):
                if 'selected_note' in st.session_state:
                    del st.session_state['selected_note']
                st.rerun()
            
            if st.button("📋 Копировать настройки", use_container_width=True):
                settings_text = f"""
{preset_name}
TYPE: {preset['type']}
VARIATION: {preset['variation']}
TONE: {preset['tone']}
DEPTH: {preset['depth']}
EFFECT: {preset['effect']}
DIRECT: {preset['direct']}
MODE: {preset['mode']}
                """
                st.code(settings_text, language="text")
            
            if st.button("🔗 Поделиться пресетом", use_container_width=True):
                st.info(f"Ссылка: boss-sy1-tuner.streamlit.app?preset={preset_name}")

else:
    st.info("👆 Начните с выбора ноты, затем выберите категорию жанра")

# Футер
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #e0e0e0;'>
    <p>🎸 Night Budva Boss SY-1 Presets | Metal • Folk • Drone Edition</p>
    <p>Создано для музыкантов с ❤️ | Данные из Boss Tone Central, Reddit, Gearspace</p>
</div>
""", unsafe_allow_html=True)
