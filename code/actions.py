import math
import re

# ---------------- NUMBER WORD MAPPING ----------------
number_map = {
    "शून्य": 0, "एक": 1, "दो": 2, "तीन": 3, "चार": 4, "पाँच": 5,
    "छह": 6, "सात": 7, "आठ": 8, "नौ": 9, "दस": 10, "ग्यारह": 11,
    "बारह": 12, "तेरह": 13, "चौदह": 14, "पंद्रह": 15, "सोलह": 16,
    "सत्रह": 17, "अठारह": 18, "उन्नीस": 19, "बीस": 20, "तीस": 30,
    "चालीस": 40, "पचास": 50, "साठ": 60, "सत्तर": 70, "अस्सी": 80,
    "नब्बे": 90, "सौ": 100
}

def words_to_numbers(text):
    words = text.split()
    numbers = []
    for word in words:
        if word in number_map:
            numbers.append(float(number_map[word]))
    return numbers

# ---------------- WORD DEFINITION ----------------
def word_definition(text):
    dictionary = {
        "कंप्यूटर": "कंप्यूटर एक इलेक्ट्रॉनिक मशीन है जो डेटा प्रोसेस करता है।",
        "इंटरनेट": "इंटरनेट एक वैश्विक नेटवर्क है जो कंप्यूटरों को जोड़ता है।",
        "लोकतंत्र": "लोकतंत्र एक शासन प्रणाली है जिसमें जनता द्वारा सरकार चुनी जाती है।",
        "संविधान": "संविधान किसी देश के नियमों और कानूनों का मुख्य दस्तावेज होता है।"
    }
    for key in dictionary:
        if key in text:
            return dictionary[key]
    return "इस शब्द का अर्थ उपलब्ध नहीं है।"

# ---------------- GENERAL KNOWLEDGE ----------------
def gk_query(text):
    gk = {
        "प्रधानमंत्री": "भारत के प्रधानमंत्री नरेंद्र मोदी हैं।",
        "ताजमहल": "ताजमहल आगरा में स्थित है।",
        "राष्ट्रीय खेल": "भारत का राष्ट्रीय खेल हॉकी है।",
        "राजधानी": "भारत की राजधानी नई दिल्ली है।"
    }
    for key in gk:
        if key in text:
            return gk[key]
    return "इस प्रश्न का उत्तर उपलब्ध नहीं है।"

# ---------------- FACTS ----------------
def facts_query(text):
    facts = {
        "भारत": "भारत दुनिया का सबसे बड़ा लोकतांत्रिक देश है।",
        "गंगा": "गंगा भारत की सबसे पवित्र नदियों में से एक है।",
        "हिमालय": "हिमालय विश्व की सबसे ऊँची पर्वत श्रृंखला है।",
        "H2O": "पानी का रासायनिक सूत्र H2O है।",
        "बल्ब": "बल्ब का आविष्कार थॉमस एडिसन ने किया।"
    }
    for key in facts:
        if key in text:
            return facts[key]
    return "इस विषय में तथ्य उपलब्ध नहीं है।"

# ---------------- HISTORY ----------------
def history_query(text):
    history = {
        "1857": "1857 की क्रांति 10 मई 1857 को शुरू हुई थी।",
        "स्वतंत्रता दिवस": "भारत का स्वतंत्रता दिवस 15 अगस्त को मनाया जाता है।",
        "महात्मा गांधी": "महात्मा गांधी का जन्म 2 अक्टूबर 1869 को हुआ था।",
        "जलियांवाला": "जलियांवाला बाग हत्याकांड 13 अप्रैल 1919 को हुआ था।"
    }
    for key in history:
        if key in text:
            return history[key]
    return "इस इतिहास प्रश्न का उत्तर उपलब्ध नहीं है।"

# ---------------- TOURISM ----------------
def tourism_query(text):
    tourist_data = {
        "दिल्ली": ["लाल किला", "कुतुब मीनार", "इंडिया गेट"],
        "मुंबई": ["गेटवे ऑफ इंडिया", "मरीन ड्राइव", "एलीफेंटा गुफाएं"],
        "चेन्नई": ["मरीना बीच", "कपालेश्वर मंदिर", "फोर्ट सेंट जॉर्ज"],
        "हैदराबाद": ["चारमीनार", "गोलकोंडा किला", "हुसैन सागर झील"]
    }
    for city in tourist_data:
        if city in text:
            return f"{city} के प्रमुख पर्यटन स्थल: {', '.join(tourist_data[city])}"
    return "इस शहर या स्थान की जानकारी उपलब्ध नहीं है।"

# ---------------- EMERGENCY ----------------
def emergency_query(text):
    emergency = {
        "पुलिस": "भारत में पुलिस का आपातकालीन नंबर 100 है।",
        "एम्बुलेंस": "एम्बुलेंस के लिए आपातकालीन नंबर 108 है।",
        "फायर": "फायर ब्रिगेड को कॉल करने का आपातकालीन नंबर 101 है।",
        "महिला हेल्पलाइन": "महिलाओं के लिए आपातकालीन हेल्पलाइन नंबर 181 है।",
        "बच्चे": "बच्चों की सहायता के लिए आपातकालीन नंबर 1098 है।",
        "सड़क दुर्घटना": "सड़क दुर्घटना की स्थिति में मदद के लिए 112 या 108 पर कॉल करें।"
    }
    for key in emergency:
        if key in text:
            return emergency[key]
    return "आपातकालीन जानकारी उपलब्ध नहीं है।"

# ---------------- WEBSITE ----------------
def website_query(text):
    websites = {
        "पैन": "PAN कार्ड के लिए आधिकारिक वेबसाइट है: https://www.onlineservices.nsdl.com",
        "आधार": "आधार कार्ड के लिए आधिकारिक वेबसाइट है: https://uidai.gov.in",
        "पासपोर्ट": "पासपोर्ट आवेदन के लिए वेबसाइट है: https://www.passportindia.gov.in",
        "ड्राइविंग लाइसेंस": "ड्राइविंग लाइसेंस के लिए वेबसाइट है: https://parivahan.gov.in"
    }
    for key in websites:
        if key in text:
            return websites[key]
    return "इस सेवा की वेबसाइट जानकारी उपलब्ध नहीं है।"

# ---------------- CALCULATION ----------------
def calculation_query(text):
    text = text.lower()
    numbers = re.findall(r'\d+\.?\d*', text)
    numbers = [float(n) for n in numbers]
    numbers.extend(words_to_numbers(text))

    if len(numbers) == 0:
        return "कृपया सही गणना दर्ज करें।"

    try:
        if "+" in text or "जोड़" in text:
            return f"उत्तर: {numbers[0] + numbers[1]}"
        elif "-" in text or "घट" in text:
            return f"उत्तर: {numbers[0] - numbers[1]}"
        elif "*" in text or "गुणा" in text:
            return f"उत्तर: {numbers[0] * numbers[1]}"
        elif "/" in text or "भाग" in text:
            return f"उत्तर: {numbers[0] / numbers[1]}"
        elif "पावर" in text:
            return f"उत्तर: {numbers[0] ** numbers[1]}"
        elif "वर्गमूल" in text:
            return f"उत्तर: {math.sqrt(numbers[0])}"
        elif "प्रतिशत" in text:
            return f"उत्तर: {(numbers[0] / 100) * numbers[1]}"
        elif "फैक्टोरियल" in text:
            return f"उत्तर: {math.factorial(int(numbers[0]))}"
        else:
            return "यह गणना उपलब्ध नहीं है।"
    except:
        return "गणना करते समय त्रुटि हुई।"

# ---------------- CONVERSION ----------------
def conversion_query(text):
    text_lower = text.lower()
    
    numbers = re.findall(r'\d+\.?\d*', text_lower)
    numbers = [float(n) for n in numbers]
    numbers.extend(words_to_numbers(text_lower))
    
    if not numbers:
        return "कृपया संख्या बताएं।"

    value = numbers[0]

    conversions = {
        "किलो से ग्राम": value * 1000,
        "ग्राम से किलो": value / 1000,
        "मीटर से सेंटीमीटर": value * 100,
        "सेंटीमीटर से मीटर": value / 100
    }

    for key in conversions:
        if all(word in text_lower for word in key.split()):
            return f"उत्तर: {conversions[key]}"

    return "यह कन्वर्जन उपलब्ध नहीं है।"

# ---------------- GREETING ----------------
def greeting():
    return "नमस्ते"

# ---------------- MAIN INTENT HANDLER ----------------
def handle_intent(intent, text):
    if intent == "WORD_DEFINITION":
        return word_definition(text)
    elif intent == "CALCULATION":
        return calculation_query(text)
    elif intent == "CONVERSION_QUERY":
        return conversion_query(text)
    elif intent == "GK_QUERY":
        return gk_query(text)
    elif intent == "FACTS_QUERY":
        return facts_query(text)
    elif intent == "HISTORY_QUERY":
        return history_query(text)
    elif intent == "TOURISM_QUERY":
        return tourism_query(text)
    elif intent == "EMERGENCY_QUERY":
        return emergency_query(text)
    elif intent == "WEBSITE_QUERY":
        return website_query(text)
    elif intent == "GREETING":
        return greeting()
    else:
        return "मुझे समझ नहीं आया।"
