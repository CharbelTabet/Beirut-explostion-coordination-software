var icons = {
    "Clusters": {
        "Over 10 damaged homes" :"https://iili.io/dvmXLb.png",
        "Over 20 damaged homes" :"https://iili.io/dvmWhu.png",
        "Over 30 damaged homes" :"https://iili.io/dvmNrQ.png",
        "Over 40 damaged homes": "https://iili.io/d8KJ6X.png",
        "Over 50 damaged homes": "https://iili.io/d8K2Fn.png",
    },
    "Damages": {
        "slightly damaged home" :"https://iili.io/d8Fi6F.png",
        "moderately damaged home" :"https://iili.io/d8FQaa.png",
        "heavily damaged home" :"https://iili.io/d8FL3g.png",
    },
    "Traffic": {
        "closed road" :"https://iili.io/d8Ftyv.png",
    },
    "Works": {
        "construction" :"https://iili.io/d8FPG1.png",
    },
    "Volunteering positions": {
        "food" :"https://iili.io/d8F6CP.png",
    },
    "Ngos": {
        "ngo" :"https://iili.io/d8FpZN.png",
        "red cross" :"https://iili.io/d8FZ8J.png",
    },
    "Warnings": {
        "SOS" :"https://iili.io/d8Fmjp.png",
        "danger" :"https://iili.io/d8FbuR.png"
    }
}

function setIcons(kind) {
    switch (kind) {
        case 'food':
            return icons["Volunteering positions"]["food"]

        case 'construction':
            return icons["Works"]["construction"]

        case 'ngo':
            return icons["Ngos"]["ngo"]

        case 'red cross':
            return icons["Ngos"]["red cross"]

        case 'danger':
            return icons["Warnings"]["danger"]
        
        case 'damage':
            return icons["Damages"]["heavily damaged home"]
    }

}
