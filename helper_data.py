# Detailed medical advice mappings for all 20 predicted diseases
DISEASE_DETAILS = {
    "Electrolyte Imbalance": {
        "symptom": "muscle cramps and weakness",
        "primary_medicine": "Electrolyte solution, Potassium supplements",
        "alternative_medicines": ["Magnesium supplements", "Calcium carbonate", "Oral Rehydration Salts (ORS)"],
        "usage_instructions": (
            "1. Take electrolyte solutions or ORS after physical workouts or if experiencing weakness.\n"
            "2. Follow dosage instructions on packaging for potassium supplements. Do not exceed the daily limit.\n"
            "3. Consume supplements with meals to prevent stomach upset."
        ),
        "precautions": [
            "Avoid intense workouts in extreme heat without proper hydration.",
            "Consult a physician if you have kidney disease before taking potassium supplements.",
            "Do not consume high-dose supplements without a blood test verification."
        ],
        "lifestyle_suggestions": [
            "Include potassium-rich foods in your diet, such as bananas, avocados, and spinach.",
            "Stay hydrated by drinking at least 2.5 - 3 liters of water daily.",
            "Reduce intake of dehydrating substances like caffeine and alcohol."
        ],
        "recovery_guidance": "Rest immediately when muscle cramps occur. Gently stretch and massage the affected muscle. Seek urgent care if you experience severe muscle pain, confusion, or an irregular heartbeat."
    },
    "Raynaud's Disease": {
        "symptom": "cold hands and feet",
        "primary_medicine": "Nifedipine, Losartan",
        "alternative_medicines": ["Diltiazem", "Amlodipine", "Sildenafil", "Ginkgo Biloba"],
        "usage_instructions": (
            "1. Take calcium channel blockers (e.g., Nifedipine) or ARBs (e.g., Losartan) exactly as prescribed by your doctor.\n"
            "2. Avoid taking calcium channel blockers with grapefruit juice.\n"
            "3. Monitor your blood pressure regularly as these medicines can cause dizziness."
        ),
        "precautions": [
            "Protect yourself from cold temperatures and rapid temperature changes.",
            "Avoid carrying heavy grocery bags by hand, which can restrict blood flow.",
            "Never smoke, as nicotine constricts blood vessels and worsens attacks."
        ],
        "lifestyle_suggestions": [
            "Wear layered clothing, warm socks, and insulated gloves in cold environments.",
            "Practice regular cardiovascular exercise to improve overall blood circulation.",
            "Use stress-reduction techniques (meditation, yoga) as emotional stress can trigger symptoms."
        ],
        "recovery_guidance": "During an attack, warm your hands and feet slowly. Place them under warm (not hot) water or wrap them in a blanket. Massage the extremities gently. Consult a doctor if skin develops sores or turns black."
    },
    "Herniated Disc": {
        "symptom": "back pain and stiffness",
        "primary_medicine": "Ibuprofen, Muscle relaxants",
        "alternative_medicines": ["Naproxen sodium", "Acetaminophen", "Cyclobenzaprine", "Gabapentin"],
        "usage_instructions": (
            "1. Take NSAIDs (Ibuprofen, Naproxen) with food or milk to protect your stomach lining.\n"
            "2. Muscle relaxants can cause significant drowsiness; take them before bedtime.\n"
            "3. Do not combine multiple pain relievers without checking with your pharmacist."
        ),
        "precautions": [
            "Avoid heavy lifting, sudden twisting movements, or bending from the waist.",
            "Limit prolonged sitting or standing in one position.",
            "Use proper lifting techniques: bend your knees and keep your back straight."
        ],
        "lifestyle_suggestions": [
            "Engage in low-impact activities like swimming or walking to keep the back flexible.",
            "Invest in an ergonomic chair with good lumbar support.",
            "Strengthen your core muscles to reduce the physical load on your spine."
        ],
        "recovery_guidance": "Apply ice packs for the first 48 hours of a flare-up to reduce inflammation, then switch to gentle heat. Perform gentle, supervised physical therapy stretches. Seek immediate care if you experience numbness in your groin or loss of bladder/bowel control."
    },
    "Migraine": {
        "symptom": "headache and nausea",
        "primary_medicine": "Sumatriptan, Naproxen",
        "alternative_medicines": ["Zolmitriptan", "Ibuprofen", "Rizatriptan", "Metoclopramide (for nausea)"],
        "usage_instructions": (
            "1. Take Sumatriptan or other triptans at the very first sign of a migraine headache.\n"
            "2. Avoid using acute pain relievers more than 2-3 days per week to prevent medication-overuse headaches.\n"
            "3. Take nausea medication 30 minutes before pain relief for maximum effectiveness."
        ),
        "precautions": [
            "Identify and avoid individual triggers (e.g., aged cheeses, chocolate, nitrates).",
            "Avoid bright lights, flashing screens, and loud noises during an attack.",
            "Keep a consistent routine for meals, hydration, and sleep."
        ],
        "lifestyle_suggestions": [
            "Keep a detailed migraine diary to track foods, weather, and sleep patterns.",
            "Manage daily stress using breathing exercises or mindfulness.",
            "Ensure regular hydration and limit caffeine intake to moderate levels."
        ],
        "recovery_guidance": "Rest in a quiet, dark, and cool room. Apply a cold compress or ice pack wrapped in a cloth to your forehead or the back of your neck. Sleep is often the most effective way to end a migraine attack."
    },
    "Bronchitis": {
        "symptom": "persistent cough with mucus",
        "primary_medicine": "Azithromycin, Cough suppressants",
        "alternative_medicines": ["Dextromethorphan", "Guaifenesin", "Amoxicillin", "Albuterol inhaler (if wheezing)"],
        "usage_instructions": (
            "1. Complete the full course of antibiotics (e.g., Azithromycin) even if you feel better.\n"
            "2. Use expectorants (Guaifenesin) during the day to thin mucus and suppressants only at night to aid sleep.\n"
            "3. Drink a full glass of water with each dose of cough medicine."
        ),
        "precautions": [
            "Stay away from tobacco smoke, dust, fumes, and chemical irritants.",
            "Avoid taking cough suppressants if you have asthma or COPD unless directed by a doctor.",
            "Wash your hands frequently to prevent spreading or catching secondary infections."
        ],
        "lifestyle_suggestions": [
            "Use a cool-mist humidifier in your bedroom to keep the air moist.",
            "Perform steam inhalation twice daily to help loosen deep chest mucus.",
            "Get plenty of rest and avoid strenuous physical activities."
        ],
        "recovery_guidance": "Drink warm liquids (herbal tea, clear broths) to soothe your throat and thin secretions. Most viral bronchitis cases resolve in 10-14 days. Seek medical attention if you develop high fever, chest pain, or cough up blood."
    },
    "Rheumatoid Arthritis": {
        "symptom": "joint pain and swelling",
        "primary_medicine": "Methotrexate, Prednisone",
        "alternative_medicines": ["Leflunomide", "Sulfasalazine", "Celecoxib", "Hydroxychloroquine"],
        "usage_instructions": (
            "1. Take Methotrexate strictly once a week on the designated day, along with Folic Acid as prescribed.\n"
            "2. Never stop Prednisone suddenly; it must be tapered off gradually under medical supervision.\n"
            "3. Take Celecoxib or other NSAIDs with food to minimize gastrointestinal discomfort."
        ),
        "precautions": [
            "Schedule regular blood tests to monitor liver and kidney function while on DMARDs.",
            "Avoid contact with individuals who have active infections since these medicines suppress your immune system.",
            "Limit alcohol intake, especially when taking Methotrexate, to avoid liver damage."
        ],
        "lifestyle_suggestions": [
            "Engage in gentle, joint-friendly exercises like swimming, water aerobics, or tai chi.",
            "Apply heat packs to stiff joints in the morning and cold packs to swollen joints after activity.",
            "Utilize ergonomic kitchen tools and assistive devices to protect hand joints."
        ],
        "recovery_guidance": "During a disease flare-up, prioritize rest and joint protection. Work closely with a rheumatologist to adjust medication. Keep joints moving gently to prevent long-term stiffness."
    },
    "Lymphadenopathy": {
        "symptom": "swollen glands in neck",
        "primary_medicine": "Amoxicillin, Analgesics",
        "alternative_medicines": ["Cephalexin", "Ibuprofen", "Acetaminophen", "Warm saline gargle"],
        "usage_instructions": (
            "1. Take Amoxicillin exactly as directed, completing the full course to prevent bacterial resistance.\n"
            "2. Use analgesics (Ibuprofen or Acetaminophen) as needed to relieve tenderness.\n"
            "3. Always check the maximum daily dose of Acetaminophen (usually 4,000mg)."
        ),
        "precautions": [
            "Do not squeeze, press, or massage the swollen lymph nodes.",
            "Avoid self-medicating with antibiotics before a doctor evaluates the swelling.",
            "Monitor the size, tenderness, and firmness of the glands daily."
        ],
        "lifestyle_suggestions": [
            "Practice good hygiene, wash hands frequently, and avoid sharing utensils.",
            "Get 8 hours of sleep each night to help your immune system fight the underlying infection.",
            "Drink plenty of water and clear fluids."
        ],
        "recovery_guidance": "Apply a warm, moist washcloth to the swollen area for 15 minutes, 3-4 times a day to relieve discomfort. Glands typically take 1 to 4 weeks to return to normal size after an infection clears. Seek immediate care if nodes become hard, fixed, or if you develop night sweats."
    },
    "Tuberculosis": {
        "symptom": "night sweats and weight loss",
        "primary_medicine": "Isoniazid, Rifampin",
        "alternative_medicines": ["Pyrazinamide", "Ethambutol", "Vitamin B6 (Pyridoxine)"],
        "usage_instructions": (
            "1. Take Isoniazid and Rifampin daily, usually on an empty stomach 1 hour before or 2 hours after meals.\n"
            "2. Take Vitamin B6 daily to prevent peripheral neuropathy caused by Isoniazid.\n"
            "3. Note that Rifampin will turn your urine, sweat, and tears an orange-red color; this is normal."
        ),
        "precautions": [
            "Avoid alcohol entirely during treatment due to the high risk of severe drug-induced liver damage.",
            "Stay isolated in a well-ventilated room during the first 2-3 weeks of active treatment.",
            "Adhere strictly to the drug regimen. Skipping doses can lead to drug-resistant TB."
        ],
        "lifestyle_suggestions": [
            "Eat a high-calorie, protein-rich diet to recover weight loss and support tissue repair.",
            "Avoid smoky, dusty, or poorly ventilated environments.",
            "Get gentle sunlight exposure to help synthesize Vitamin D."
        ],
        "recovery_guidance": "TB recovery is a long journey requiring 6 to 9 months of treatment. Get regular sputum tests and liver function tests. Rest as much as possible, eat healthy meals, and complete your medications even if symptoms completely disappear."
    },
    "Gastroenteritis": {
        "symptom": "diarrhea and stomach cramps",
        "primary_medicine": "Loperamide, Oral Rehydration",
        "alternative_medicines": ["Bismuth subsalicylate", "Probiotics", "Ondansetron (for vomiting)", "Zinc supplements"],
        "usage_instructions": (
            "1. Dissolve ORS packets in clean water according to instructions and drink small sips throughout the day.\n"
            "2. Use Loperamide sparingly; do not take it if you have high fever or bloody diarrhea (signs of bacterial infection).\n"
            "3. Take probiotics to restore healthy gut flora once vomiting stops."
        ),
        "precautions": [
            "Avoid dairy products, high-sugar beverages, greasy foods, and caffeine.",
            "Wash your hands with soap and water after using the restroom and before preparing food.",
            "Do not prepare food for others while you are actively sick and for 48 hours after recovery."
        ],
        "lifestyle_suggestions": [
            "Follow the BRAT diet (Bananas, Rice, Applesauce, Toast) once your stomach tolerates food.",
            "Sanitize shared household surfaces like doorknobs, faucets, and light switches.",
            "Drink diluted broth or weak decaffeinated teas."
        ],
        "recovery_guidance": "Focus on continuous hydration. Let your stomach rest for a few hours after vomiting before attempting to drink or eat. Seek emergency care if you cannot keep liquids down for 24 hours, experience extreme dizziness, or have blood in your stools."
    },
    "Type 2 Diabetes": {
        "symptom": "tiredness and frequent urination",
        "primary_medicine": "Metformin, Glipizide",
        "alternative_medicines": ["Empagliflozin", "Sitagliptin", "Pioglitazone", "Alpha-lipoic acid"],
        "usage_instructions": (
            "1. Take Metformin with your largest meals to minimize stomach upset and diarrhea.\n"
            "2. Take Glipizide 30 minutes before your first meal of the day.\n"
            "3. Always keep a quick source of sugar (like fruit juice or glucose tablets) nearby if taking insulin or sulfonylureas."
        ),
        "precautions": [
            "Learn to recognize symptoms of hypoglycemia (low blood sugar): shakiness, sweating, confusion, irritability.",
            "Inspect your feet daily for cuts, sores, or blisters, as diabetes reduces sensation and slows healing.",
            "Check your blood glucose levels regularly as instructed by your doctor."
        ],
        "lifestyle_suggestions": [
            "Follow a balanced diet rich in fiber, vegetables, and lean protein, while limiting refined carbs and sugar.",
            "Aim for at least 150 minutes of moderate-intensity physical exercise (like brisk walking) per week.",
            "Maintain a healthy weight through portion control and active living."
        ],
        "recovery_guidance": "Type 2 Diabetes is a chronic condition that requires consistent daily self-management. Have regular HbA1c tests every 3-6 months. Partner with a primary care doctor, endocrinologist, and certified diabetes educator."
    },
    "Meningitis": {
        "symptom": "sensitivity to light and headaches",
        "primary_medicine": "Ceftriaxone, Dexamethasone",
        "alternative_medicines": ["Meropenem", "Vancomycin", "Acyclovir (if viral meningitis)", "Intravenous fluids"],
        "usage_instructions": (
            "1. These medications are administered intravenously in a hospital or clinical setting.\n"
            "2. Dexamethasone (a steroid) is given before or with the first dose of antibiotics to reduce brain swelling.\n"
            "3. Complete the intravenous course as prescribed by the medical team."
        ),
        "precautions": [
            "Bacterial meningitis is a medical emergency. Do not wait to see if symptoms improve.",
            "Close contacts (family, roommates) may require preventive antibiotics (chemoprophylaxis).",
            "Avoid sharing food, drinks, or toothbrushes."
        ],
        "lifestyle_suggestions": [
            "Ensure that vaccinations (meningococcal, pneumococcal, Hib) are up to date.",
            "Rest in a quiet, dark room to minimize photophobia (light sensitivity) during recovery.",
            "Maintain a balanced diet and stay hydrated once discharged from the hospital."
        ],
        "recovery_guidance": "Meningitis requires immediate emergency hospital care. Post-discharge, physical therapy and cognitive rehabilitation may be necessary depending on the severity. Attend all neurological and hearing follow-up appointments."
    },
    "Dehydration": {
        "symptom": "dry mouth and excessive thirst",
        "primary_medicine": "ORS, IV Fluids",
        "alternative_medicines": ["Electrolyte tablets", "Coconut water", "Diluted sports drinks"],
        "usage_instructions": (
            "1. Sip Oral Rehydration Salts (ORS) slowly in small, frequent amounts rather than gulping them down.\n"
            "2. For mild dehydration, consume 1-2 liters of water or ORS over a few hours.\n"
            "3. Severe dehydration requires professional medical administration of IV fluids."
        ),
        "precautions": [
            "Avoid drinking highly sugary drinks, sodas, alcohol, or strong coffee, which can worsen dehydration.",
            "Do not perform heavy exercise in high temperatures during recovery.",
            "Monitor urine output. If you stop urinating or your urine is very dark, seek medical help."
        ],
        "lifestyle_suggestions": [
            "Always carry a reusable water bottle and drink fluids regularly throughout the day.",
            "Increase fluid intake during hot weather, fever, vomiting, or diarrhea.",
            "Eat water-dense foods like watermelons, cucumbers, strawberries, and oranges."
        ],
        "recovery_guidance": "Rest in a cool, shaded area. Drink fluids steadily. Mild dehydration resolves within a few hours of adequate fluid intake, while severe cases may take a day or two of IV therapy. Monitor your recovery using urine color (aim for pale straw yellow)."
    },
    "Glaucoma": {
        "symptom": "blurred vision and eye pain",
        "primary_medicine": "Latanoprost, Timolol",
        "alternative_medicines": ["Brimonidine", "Dorzolamide", "Pilocarpine", "Coenzyme Q10"],
        "usage_instructions": (
            "1. Apply Latanoprost drops in the evening. Keep your eyes closed for 1-2 minutes after applying.\n"
            "2. Use Timolol (beta-blocker) drops exactly at the scheduled times. Press the tear duct to reduce systemic absorption.\n"
            "3. Wait at least 15 minutes before inserting contact lenses after using eye drops."
        ),
        "precautions": [
            "Never skip a dose or stop using your eye drops, as eye pressure can rise rapidly without symptoms.",
            "Consult your ophthalmologist immediately if you experience sudden, severe eye pain or red eye.",
            "Avoid rubbing your eyes or using non-prescription eye drops."
        ],
        "lifestyle_suggestions": [
            "Receive comprehensive dilated eye exams every 6-12 months.",
            "Limit caffeine intake as high amounts can temporarily increase intraocular pressure.",
            "Avoid sleeping with your face pressed against the pillow or head lower than the body."
        ],
        "recovery_guidance": "Glaucoma is a lifetime condition. The goal of treatment is to control eye pressure to prevent further vision loss (it cannot reverse existing damage). Strictly follow your treatment plan and schedule regular visual field tests."
    },
    "Pharyngitis": {
        "symptom": "sore throat and mild fever",
        "primary_medicine": "Paracetamol, Lozenges",
        "alternative_medicines": ["Ibuprofen", "Throat sprays", "Warm saline gargle", "Amoxicillin (if streptococcal)"],
        "usage_instructions": (
            "1. Take Paracetamol (Acetaminophen) every 4-6 hours as needed for fever and throat pain. Do not exceed 4g/day.\n"
            "2. Dissolve throat lozenges slowly in your mouth. Avoid giving them to children under 4 years old.\n"
            "3. If a doctor diagnoses strep throat and prescribes antibiotics, take them for the entire duration."
        ),
        "precautions": [
            "Avoid extremely hot, cold, or highly acidic foods and beverages which can irritate your throat.",
            "Restrict talking to rest your vocal cords.",
            "Do not share cups, straws, or utensils with others."
        ],
        "lifestyle_suggestions": [
            "Gargle with warm salt water (1/2 teaspoon of salt in a glass of warm water) 3-4 times daily.",
            "Drink warm teas with honey (do not give honey to children under 1 year old).",
            "Use a room humidifier to keep the throat from drying out."
        ],
        "recovery_guidance": "Pharyngitis is usually viral and resolves on its own in 5 to 7 days. Ensure plenty of bed rest and fluid intake. Consult a doctor if you develop a high fever, severe difficulty swallowing, or breathing problems."
    },
    "Acid Reflux": {
        "symptom": "abdominal pain and bloating",
        "primary_medicine": "Omeprazole, Ranitidine",
        "alternative_medicines": ["Famotidine", "Antacid tablets (Calcium carbonate)", "Esomeprazole", "Ginger tea"],
        "usage_instructions": (
            "1. Take proton pump inhibitors (e.g., Omeprazole) in the morning, 30-60 minutes before breakfast.\n"
            "2. Take H2 blockers (e.g., Famotidine) before evening meals or at bedtime.\n"
            "3. Antacids can be chewed as needed for immediate, short-term relief after meals."
        ),
        "precautions": [
            "Do not lie down within 2 to 3 hours after eating a meal.",
            "Avoid wearing tight clothing or belts that compress your abdomen.",
            "Limit or avoid triggers: spicy, fatty, fried, citrus, chocolate, peppermint, and tomato-based foods."
        ],
        "lifestyle_suggestions": [
            "Eat smaller, more frequent meals instead of two or three large meals.",
            "Elevate the head of your bed by 6 to 8 inches using bed risers or a wedge pillow.",
            "Maintain a healthy weight to reduce pressure on the lower esophageal sphincter."
        ],
        "recovery_guidance": "Acid reflux symptoms can be managed effectively with dietary and lifestyle adjustments combined with short-term medication. If symptoms persist or you experience difficulty swallowing, chronic cough, or unexplained weight loss, consult a gastroenterologist."
    },
    "Heart Disease": {
        "symptom": "chest pain and dizziness",
        "primary_medicine": "Aspirin, Nitroglycerin",
        "alternative_medicines": ["Metoprolol", "Atorvastatin", "Clopidogrel", "Coenzyme Q10"],
        "usage_instructions": (
            "1. Take low-dose Aspirin daily if prescribed. Do not stop without consulting your cardiologist.\n"
            "2. Place Nitroglycerin under your tongue (sublingually) at the onset of chest pain. Let it dissolve; do not swallow.\n"
            "3. Rest immediately after taking Nitroglycerin, as it can cause a rapid drop in blood pressure."
        ),
        "precautions": [
            "If chest pain persists after one dose of Nitroglycerin (or after 5 minutes), call emergency services immediately.",
            "Monitor your heart rate and blood pressure regularly.",
            "Avoid strenuous physical activities that cause shortness of breath or chest discomfort."
        ],
        "lifestyle_suggestions": [
            "Adopt a heart-healthy diet like the Mediterranean diet, focusing on whole grains, vegetables, fish, and olive oil.",
            "Stop smoking immediately and avoid secondhand exposure.",
            "Engage in structured, moderate physical activity (such as daily walking) as approved by your physician."
        ],
        "recovery_guidance": "Heart disease is a serious, long-term condition. Complete cardiac rehabilitation programs if recommended. Take all medications exactly as directed. Regular check-ups with your cardiologist are crucial."
    },
    "Eczema": {
        "symptom": "itchy skin and rash",
        "primary_medicine": "Hydrocortisone, Moisturizers",
        "alternative_medicines": ["Tacrolimus ointment", "Antihistamines (cetirizine, diphenhydramine)", "Ceramide-rich creams"],
        "usage_instructions": (
            "1. Apply Hydrocortisone cream sparingly to affected areas 1-2 times daily during flare-ups. Limit use on face.\n"
            "2. Apply thick moisturizers (ointment or cream, not lotion) within 3 minutes of bathing to lock in moisture.\n"
            "3. Use oral antihistamines at night if itching prevents sleep."
        ),
        "precautions": [
            "Avoid scratching the skin. Keep fingernails short and clean to prevent secondary bacterial infections.",
            "Do not use harsh soaps, bubble baths, or products containing alcohol and artificial fragrances.",
            "Avoid sudden changes in temperature or humidity that can trigger sweating."
        ],
        "lifestyle_suggestions": [
            "Take short, lukewarm showers or baths (no longer than 10-15 minutes).",
            "Wear soft, breathable cotton fabrics; avoid wool and synthetic fibers.",
            "Use a gentle, fragrance-free laundry detergent and double rinse clothes."
        ],
        "recovery_guidance": "Eczema is a relapsing skin condition. Focus on daily skin barrier maintenance by moisturizing 2-3 times a day. If skin becomes hot, painful, weeping, or yellow-crusted, consult a dermatologist as these are signs of infection."
    },
    "Asthma": {
        "symptom": "shortness of breath and cough",
        "primary_medicine": "Salbutamol, Fluticasone",
        "alternative_medicines": ["Albuterol inhaler", "Montelukast", "Budesonide", "Levalbuterol"],
        "usage_instructions": (
            "1. Use Salbutamol (blue rescue inhaler) for quick relief of acute breathing difficulty or before exercise.\n"
            "2. Use Fluticasone (preventer inhaler) daily as prescribed, even if you feel completely fine.\n"
            "3. Always rinse your mouth with water and spit it out after using steroid inhalers (like Fluticasone) to prevent oral thrush."
        ),
        "precautions": [
            "Always carry your quick-relief rescue inhaler (Salbutamol) with you.",
            "Avoid exposure to known triggers: dust mites, pollen, mold, pet dander, tobacco smoke, and cold air.",
            "Do not use beta-blocker medications or aspirin without consulting your doctor, as they can trigger asthma attacks."
        ],
        "lifestyle_suggestions": [
            "Use allergen-proof covers on pillows and mattresses. Vacuum carpets frequently.",
            "Monitor your breathing using a peak flow meter and follow your Asthma Action Plan.",
            "Perform breathing exercises (like pranayama or Buteyko method) to help regulate breathing patterns."
        ],
        "recovery_guidance": "Manage asthma actively through daily controller medications. Keep a rescue log. Seek emergency room care if your breathing does not improve after using your rescue inhaler, if you struggle to speak in full sentences, or if your nails/lips turn blue."
    },
    "Hypertension": {
        "symptom": "frequent nosebleeds",
        "primary_medicine": "Lisinopril, Amlodipine",
        "alternative_medicines": ["Losartan potassium", "Metoprolol succinate", "Hydrochlorothiazide", "Garlic extract"],
        "usage_instructions": (
            "1. Take blood pressure medications daily at the same time. Do not skip doses.\n"
            "2. If taking a diuretic (like Hydrochlorothiazide), take it in the morning to avoid waking up at night to urinate.\n"
            "3. Stand up slowly from sitting or lying positions, as these medications can cause orthostatic dizziness."
        ),
        "precautions": [
            "Do not stop taking your blood pressure medications suddenly; this can cause a dangerous rebound in blood pressure.",
            "Avoid over-the-counter decongestants or nasal sprays (like oxymetazoline), as they can raise blood pressure.",
            "Limit sodium (salt) intake to less than 1,500 - 2,000 mg per day."
        ],
        "lifestyle_suggestions": [
            "Follow the DASH (Dietary Approaches to Stop Hypertension) diet, rich in fruits, vegetables, and low-fat dairy.",
            "Incorporate at least 30 minutes of aerobic exercise (like cycling, walking) into your daily routine.",
            "Practice stress-management techniques (deep breathing, yoga, spending time in nature)."
        ],
        "recovery_guidance": "Hypertension is often a symptomless condition ('the silent killer') but can manifest as frequent nosebleeds in severe cases. Keep a daily blood pressure log. Regular cardiovascular examinations and blood tests are needed to monitor kidney function."
    },
    "Insomnia": {
        "symptom": "difficulty sleeping",
        "primary_medicine": "Melatonin, Zolpidem",
        "alternative_medicines": ["Diphenhydramine", "Eszopiclone", "Valerian Root extract", "Chamomile tea"],
        "usage_instructions": (
            "1. Take Melatonin 30 to 60 minutes before your planned bedtime.\n"
            "2. Take Zolpidem immediately before going to bed, and only when you can dedicate 7-8 hours to sleep.\n"
            "3. Zolpidem is prescription-only and should be used for short durations (usually less than 2-4 weeks) to avoid dependency."
        ),
        "precautions": [
            "Do not drive or operate machinery after taking sleep medications.",
            "Avoid mixing sleep aids with alcohol or other central nervous system depressants.",
            "Do not take a dose of Zolpidem in the middle of the night."
        ],
        "lifestyle_suggestions": [
            "Maintain a consistent sleep schedule: go to bed and wake up at the same time every day, even on weekends.",
            "Create a dark, quiet, and cool bedroom environment (ideal temperature is around 65°F/18°C).",
            "Avoid screens (smartphones, TVs) at least 1 hour before bed, and restrict caffeine and heavy meals in the evening."
        ],
        "recovery_guidance": "For chronic insomnia, Cognitive Behavioral Therapy for Insomnia (CBT-I) is the recommended first-line treatment and is more effective long-term than sleep medications. Work on stimulus control and sleep hygiene."
    }
}
