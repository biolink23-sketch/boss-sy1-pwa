// База данных пресетов Boss SY-1
const PRESETS = {
    "Classic Lead Synth": {
        type: "LEAD 1",
        variation: 3,
        tone_rate: 7,
        depth: 5,
        effect: 8,
        direct: 3,
        guitar_bass: "GUITAR",
        description: "Классический лид-синтезатор для соло"
    },
    "Fat Bass Synth": {
        type: "BASS",
        variation: 5,
        tone_rate: 4,
        depth: 6,
        effect: 9,
        direct: 2,
        guitar_bass: "BASS",
        description: "Жирный бас-синтезатор"
    },
    "Analog Pad": {
        type: "PAD",
        variation: 2,
        tone_rate: 6,
        depth: 7,
        effect: 7,
        direct: 4,
        guitar_bass: "GUITAR",
        description: "Мягкий аналоговый пад"
    },
    "Vintage Strings": {
        type: "STR",
        variation: 4,
        tone_rate: 5,
        depth: 5,
        effect: 8,
        direct: 5,
        guitar_bass: "GUITAR",
        description: "Винтажные струнные"
    },
    "Hammond Organ": {
        type: "ORGN",
        variation: 6,
        tone_rate: 8,
        depth: 4,
        effect: 9,
        direct: 3,
        guitar_bass: "GUITAR",
        description: "Классический орган Hammond"
    },
    "Bell Tower": {
        type: "BELL",
        variation: 7,
        tone_rate: 6,
        depth: 6,
        effect: 7,
        direct: 4,
        guitar_bass: "GUITAR",
        description: "Колокольный звон"
    },
    "Laser Zap": {
        type: "SFX 1",
        variation: 9,
        tone_rate: 9,
        depth: 8,
        effect: 10,
        direct: 1,
        guitar_bass: "GUITAR",
        description: "Лазерные эффекты"
    },
    "Arpeggiator": {
        type: "SEQ 1",
        variation: 8,
        tone_rate: 7,
        depth: 7,
        effect: 8,
        direct: 3,
        guitar_bass: "GUITAR",
        description: "Арпеджиатор"
    },
    "Octave Lead": {
        type: "LEAD 2",
        variation: 10,
        tone_rate: 8,
        depth: 6,
        effect: 9,
        direct: 4,
        guitar_bass: "GUITAR",
        description: "Лид с октавой вверх"
    },
    "Sub Bass": {
        type: "BASS",
        variation: 1,
        tone_rate: 3,
        depth: 8,
        effect: 10,
        direct: 2,
        guitar_bass: "BASS",
        description: "Суб-бас для низких частот"
    },
    "Ambient Pad": {
        type: "PAD",
        variation: 11,
        tone_rate: 5,
        depth: 9,
        effect: 6,
        direct: 5,
        guitar_bass: "GUITAR",
        description: "Эмбиент пад для атмосферы"
    },
    "Sci-Fi Sweep": {
        type: "SFX 2",
        variation: 6,
        tone_rate: 10,
        depth: 9,
        effect: 9,
        direct: 2,
        guitar_bass: "GUITAR",
        description: "Научно-фантастические свипы"
    }
};

// Ноты и их частоты
const NOTE_FREQUENCIES = {
    'C': [16.35, 32.70, 65.41, 130.81, 261.63, 523.25, 1046.50, 2093.00, 4186.01],
    'C#': [17.32, 34.65, 69.30, 138.59, 277.18, 554.37, 1108.73, 2217.46, 4434.92],
    'D': [18.35, 36.71, 73.42, 146.83, 293.66, 587.33, 1174.66, 2349.32, 4698.63],
    'D#': [19.45, 38.89, 77.78, 155.56, 311.13, 622.25, 1244.51, 2489.02, 4978.03],
    'E': [20.60, 41.20, 82.41, 164.81, 329.63, 659.25, 1318.51, 2637.02, 5274.04],
    'F': [21.83, 43.65, 87.31, 174.61, 349.23, 698.46, 1396.91, 2793.83, 5587.65],
    'F#': [23.12, 46.25, 92.50, 185.00, 369.99, 739.99, 1479.98, 2959.96, 5919.91],
    'G': [24.50, 49.00, 98.00, 196.00, 392.00, 783.99, 1567.98, 3135.96, 6271.93],
    'G#': [25.96, 51.91, 103.83, 207.65, 415.30, 830.61, 1661.22, 3322.44, 6644.88],
    'A': [27.50, 55.00, 110.00, 220.00, 440.00, 880.00, 1760.00, 3520.00, 7040.00],
    'A#': [29.14, 58.27, 116.54, 233.08, 466.16, 932.33, 1864.66, 3729.31, 7458.62],
    'B': [30.87, 61.74, 123.47, 246.94, 493.88, 987.77, 1975.53, 3951.07, 7902.13]
};
