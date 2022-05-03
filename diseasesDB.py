# Disease name
# Symptoms
# Causes
# Cure

# more information
# Doctors

import sqlite3


def add_many(List):
    conn = sqlite3.connect('disease.db')
    c = conn.cursor()
    for item in List:
        c.execute("INSERT INTO diseases VALUES (?,?,?,?)", item)
    conn.commit()
    conn.close()


stuff = [
    ("Acidity",
     "",
     """Common Causes:
     Consumption of alcohol
     Highly spicy foodstuffs
     Non-vegetarian diets
     Non-Steroidal Anti-Inflammatory Drugs (NSAID's)""",
     """Home Remedies:
     After all three meals, take a small piece of jaggery and keep it in your mouth and suck. Voilá no more acidity.
     Boil one cup of water. To this add 1 tsp of aniseed (Saunf). Cover and leave overnight. Strain the water in the morning, add 1 tsp of honey. When this is taken 3 times a day it prevents acidity.
     Powder one clove and one cardamom; use the powder as a mouth freshener after every meal. No more acidity and no more bad breath.""",
     ),
    ("Acne",
     "",
     """Common causes:
     Secretion of an excessive amount of oil in the skin
     Hormonal changes during puberty
     Accumulation of oily secretions on the skin surface
     Blockage of the external pores in the skin
     Stress""",
     """Home Remedies:
     Fresh lime juice may be dabbed on pimples and blackheads.
     Make a paste of fresh, young curry leaves apply and keep on overnight wash with warm water in the morning. Helps wrinkles to fade away gradually.
     For dry skin rub a piece of sandalwood on a smooth stone with a few drops of raw milk. Apply the paste procured on affected areas. Keep on for 1 hour. Gently wash.""",
     ),
    ("Age_Spots",
     "",
     """Causes:
     Overexposure of skin to sun rays causes increased production of melanin to protect the inner layers of skin from harmful UV rays.
     Prolonged use of electronic tanning lamps and tanning beds can also cause skin darkening. Aging, chronic illness and poor nutrition are also contributing factors for age spots.""",
     """Home Remedies:
     Lemon Juice: Lemon juice is one of the best remedies to reduce age spots.
     Aloe Vera: Aloe Vera juice or gel is another good treatment for age spots. It helps clear marks and diminishes dark spots effectively.""",
     ),
    ("""Alcoholism""",
     """""",
     """Common Causes:
     Depression
     Schizophrenia
     Established behavior patterns
     Environment
     Damaged relationships
     """,
     """Home Remedies:
     First and foremost, the person should be willing to give up alcohol. Sadly, but very true that the only way to do it is, to make a clean break.
     Eating as many apples as possible at regular intervals can, reduce your craving for alcohol. They also help to clear the toxins from the system.
     Grapes contain a pure form of alcohol. A person wanting to give up this habit should have a meal of grapes every 4-5 hours, for a month at least.
     """
     ),
    ("""Anemia""",
     """""",
     """Common Causes:
     Bleeding (hemorrhage)
     Iron deficiency
     Body inability to produce sufficient red blood cells
     Hemolysis
     Pregnancy
     Menstruation
     Piles
     Hiatus hernia
     Hookworm infestation""",
     """Home Remedies:
     1 Cup beetroot juice, 1 cup of apple juice, mixed with either sugar or honey once a day.
     Consume a ripe banana with 1 tbsp of honey 2 times a day.
     Soak 10 currants overnight. Remove seeds and have for 3-4 weeks early in the morning.
     """),
    ("""Anorexia""",
     """""",
     """Common Causes:
     Dieting
     Emotional problems
     Genes
     Imbalance of chemicals in the brain
     """,
     """Home Remedies:
     Boil 2-3 cloves of garlic in 1 cup of water. Strain. Add the juice of ½ a lime to this and drink 2 times a day, for a week.
     Make a paste of fresh Ginger. Add a pinch of salt and a drop of lime juice to ½ a tspn of the paste. Eat this 2 times a day for 1 week.
     Eat at least 1 Apple a day."""),
    ("""Appendicitis""",
     """Symptoms:
     Sharp pain in lower right abdomen Coughing or sneezing increases abdominal pain.
     Inability to pass gas (break wind, fart)
     Painful urination Severe cramps
     Loss of appetite
     Constipation""",
     """""",
     """Home Remedies:
     Drinking plenty of water throughout the day is essential for a healthy appendix.
     Prepare a cup of ginseng tea and have it twice daily, as it helps in curing the pain and inflammation of the appendix.
     Green gram is an effective remedy for treating appendicitis. Take 1 tablespoon of green gram soaked in water thrice daily.
     Consume equal quantity of honey and lemon juice to prevent indigestion during appendicitis.
     Buttermilk is very effective in preventing the bacterial growth in the appendix. Consume a liter of buttermilk daily."""
     ),
    ("""Asthma""",
     """""",
     """Common Causes:
     Allergy to pollen, dust particles
     Ait pollution
     Respiratory infections
     Sulfites in food""",
     """Home Remedies:
     Mix 1 tsp of honey with ½ tsp of cinnamon powder. Consume the mixture just before sleeping to treat asthma.
     Boil 8-10 cloves of garlic in ½ cup of milk. Have it at night, as it is good for the early stages of asthma.
     Figs are good for draining phlegm. Wash 3-4 dry figs with water. Soak in 1 cup of water. Eat these on an empty stomach and drink the water that the figs were soaked in also. Do not eat anything else for an hour at least. Do this for 2 months"""
     ),
    ("""Back_Pain""",
     """""",
     """Common Causes:
     Slipped disc and fracture in bones are the most common injuries resulting in back pain.
     Over Straining of Back Muscles
     Arthritis
     Skeletal Irregularities""",
     """Home Remedies:
     Core Strengthening Exercises
     Body Weight Management
     Boost Calcium Intake
     Sleep Properly"""),
    ("""Bad_Breath""",
     """""",
     """Common Causes:
     Bad dental hygiene is one of the main reasons of bad breath. When food particles are stuck between tooth cavities they can smell bad.
     Gum disease-gingivitis- is also a major cause and a dentist should be consulted at the earliest.
     Constipation and an upset stomach also cause bad breath.""",
     """Home Remedies:
     Brush teeth two to three times a day.
     Mix 1 teaspoon of salt to a glass of water and gargle with this three times a day.
     Mix ½ teaspoon salt to 1 teaspoon of mustard oil and massage the gums with this, it tightens the gums and prevents gum disease and keep away bad breath."""
     ),
    ("""Bedwetting""",
     """""",
     """Common Causes:
     Inability to wake up from sleep
     Overactive bladder
     Constipation
     Genetic factors""",
     """Home Remedies:
     Urinate twice before going to bed
     Reduce liquid consumption in the evening (deprivation)""",
     ),
    ("""Body_Odor""",
     """""",
     """Common Causes:
     Moist and warm environments aid bacterial and fungal growth, providing them perfect temperatures to multiply.
     Stress, anxiety, menstruation in women and anger cause increased sweating and therefore more odor.""",
     """Home Remedies:
     Bathing and proper cleaning of body is necessary to avoid growth of bad smelling microorganisms.
     Vinegar lowers body pH that stops bacteria from multiplying as they cannot survive in acidic environment
     A mix of 4-5 essential oils can act as homemade deodorant that leave your body fragrant, sweat free and fresh."""
     ),
    ("""BP-High""",
     """""",
     """Common Causes:
     Obesity
     Abnormal blood vessels
     Genetic factors
     Excessive alcohol""",
     """Home Remedies:
     Carrots, Spinach and Parsley to Keep Blood Pressure Under Control
     Indian gooseberry (Amla) is an effective home remedy for high blood pressure.
     Ginger Juice with Honey and Cumin Powder for High Blood Pressure"""
     ),
    ("""BP-Low""",
     """""",
     """Common Causes:
     Dehydration (due to sweating and/or diarrhea)
     Medications (for high BP or other treatments
     Pregnancy
     Fainting""",
     """Home Remedies:
     Soak 32 small raisins in a ceramic bowl full of water over night. Chew them one by one first thing in the morning. Chew well and drink the water also.
     Soak 7 almonds in water over night. Peel them and grind to a smooth paste. Add in a glass of milk and boil. Drink warm.
     Crush 10-15 holy basil leaves (tulsi) and strain through a clean muslin cloth. Mix with 1 tsp honey. Have it the first thing in the morning."""
     ),
    ("""Tooth_Ache""",
     """""",
     """Common Causes:
     Tooth pain occurs due to various causes including tooth decay or cavities, abscesses, broken or damaged teeth, sinus infections and gum disease.
     In a broken tooth, the outer hard tissues are cracked and movement such as chewing can lead to the movement of the pieces which irritates the pulp.
     """,
     """Home Remedies:
     Lime is also an effective home remedy for toothache and promotes the general health of the teeth
     The antiseptic properties of clove oil have made it one of the most popular home remedies for tooth infection pain. It numbs the affected teeth and gums thus relieving the pain.
     Babool tree bark is an excellent Ayurvedic herbal home remedy which can take care of the pain. It is also used to stop any bleeding in the tooth."""
     ),
    ("""Bronchitis""",
     """Symptoms:
     Persistent cough, chest pains, tiredness, fevers, difficulty in breathing and mucus production.
     Presence of Blood in mucus.""",
     """Common causes:
     Acute bronchitis is a viral infection. At times it is also caused by a bacterial infection though it’s not very common.
     Cigarette smoking is one of the chief causes of chronic bronchitis.
     Inhalation of polluted air due to the presence of toxic gases, industrial fumes or sulfur dioxide can also cause bronchitis.""",
     """Home Remedies:
     Inhalation of steam helps clear phlegm and mucus from the bronchial tubes and lungs.
     Ginger contains anti-inflammatory properties, which help clear mucus from lungs.
     Honey is packed with mineral and enzymes that help clear out infections from the body and reduce inflammations."""
     ),
    ("""Burns""",
     """Prevention:
     Store gasoline, lighter fluid and other highly flammable materials in a safe and secure container.
     Do not smoke in bed.
     Keep a fire extinguisher in an easily accessible spot in your kitchen.""",
     """Dos and Don'ts:
     Don’t use ice or an ice pack for burns; instead, hold it under cold running water for 5 to 10 minutes. If this is not possible, immerse the burn in cool water or use a cold compress.
     Don’t use butter, grease or any type of oil on the burn; instead, apply a first aid cream for burns to the area
     Don’t use cotton or any fluffy dressing to cover the burn; instead, lightly bind the area with a sterile gauze bandage.""",
     """Home Remedies:
     Apply a thin layer of honey to a strip of gauze and use this to bandage your burn.
     Aloe vera is another popular herb that is often touted as the cure to all problems.
     Refrigerate a couple of used tea bags and then place them over the burn. Use a clean strip of gauze to hold them in place. This remedy will reduce the pain and inflammation."""
     ),
    ("""Chapped_Lips""",
     """""",
     """Common Causes:
     Dehydration
     Licking Lips
     Allergens""",
     """Home Remedies:
     Papaya acts as a natural exfoliant. Apply mashed, ripe papaya to the lips and rinse off after 10 minutes.
     Gently rub a small slice of cucumber across your dry lips and leave it for 15- 20 minutes and then wash lips with water.
     Topical application of aloe vera gel, olive oil, mustard oil or coconut oil multiple times in a day function as natural moisturizers.""",
     ),
    ("""Chest_Congestion""",
     """""",
     """Common Causes:
     Chest congestion due to bronchitis may be caused due to many factors such as infection, or irritation from fumes, dust or pollutants in the environment
     There are various risk factors, which may lead to chest congestion such as smoking, reduced immunity or pre-existing condition of asthma.""",
     """Home Remedies:
     Anise has expectorant and has antibacterial properties, and aids in soothing the throat. Therefore, it is an important constituent of several cough syrups and lozenges.
     Camphor is an essential ingredient in various products that are applied locally and is available as an over-the-counter medicine for chest congestion. 
     An important ingredient of many cold rubs and balms, eucalyptus is another great herbal remedy for chest congestion.""",
     ),
    ("""Chickenpox""",
     """""",
     """Common causes:
     Herpes Zoster Virus
     Poor immune system
     Contact with broken Chickenpox blisters""",
     """Home Remedies:
     Mix ½ tsp of baking soda in 1 glass of water. Sponge the person with this solution. When soda dries on the skin, it controls the itchiness and irritation.
     Pure honey smeared on the scabs helps in clearing up scars.
     Application of vitamin E oil helps and has a healing effect. The scars fade away very quickly.""",
     ),
    ("""Cold""",
     """""",
     """Common Causes:
     Viruses (especially, rhinoviruses and coronaviruses)
     Allergic disorders
     Person to person (through cough, sneezing or hand contact)""",
     """Home Remedies
     Lots of rest - Resting conserves energy in the body. Infants, when allowed to sleep well, are able to activate their immune system to tackle the infection.
     Drink lots of fluids - Warm milk, water, diluted juice
     A saline solution can be sprayed or used as drops in the nose to clear out the mucus in the nasal passages, and thus relieve congestion.""",
     ),
    ("""Constipation""",
     """""",
     """Common Causes:
     Low fiber diet, Low fluid intake, Lack of exercise,
     Weak bowel muscles, Hemorrhoids,
     Excessive intake of calcium or iron, Irritable bowel syndrome""",
     """Home Remedies:
     Fruit juices such as those of prune, pear or apple help soften the stool. Do not give prune juice to infants, even if it is watered down; it serves as an irritant. 
     High fiber foods can help ease the passage of stool and relieve constipation. 
     Adequate fluids are necessary to resolve constipation.""",
     ),
    ("""Corns""",
     """""",
     """Common Causes:
     Increased skin pressure
     Deformed toes
     Rubbing of the toe against the stitch inside the shoe""",
     """Home Remedies
     Chalk, powdered and made into a paste by adding water, is very effective when applied on corn at bedtime.
     Liquorice powdered and mixed with either mustard or sesame oil (Gingili oil) to make a paste should be applied on the corns 2-3 times a day.
     Pumice stones are useful for treating corns. Rub this pumice stone on wet and moist feet after having a warm bath""",
     ),
    ("""Cough""",
     """""",
     """Common Causes:
     Viral Infection, Flu, Smoking
     Asthma, Tuberculosis, clot in lung, Pneumonia""",
     """Home Remedies:
     Take 3 peppercorns with a pinch of black cumin seeds (shah jeera) and a pinch of salt.
     3-5 drops of clove oil mixed with a clove of crushed garlic and ½ tsp honey helps soothe the throat
     In a cup of boiling water add 1 tsp turmeric powder and 1 tsp carom seeds (ajwain). Boil till half. Add 1 tsp of honey and have 2 times a day.""",
     ),
    ("""Dandruff""",
     """""",
     """Common Causes:
     Yeast sensitivity
     Dry Skin
     Seborrheic Dermatitis""",
     """Home Remedies:
     It is believed that brushing your hair right after shampoo can help curb dandruff problems.
     Coconut oil is one of the best and widely used home remedies to cure dandruff.
     Fenugreek seeds can be a good natural anit-dandruff agent.""",
     ),
    ("""Depression""",
     """""",
     """Common Causes:
     Change in brain structures or brain functions
     Pessimistic attitude
     Stress, Hormonal disorders, Financial problems""",
     """Home Remedies:
     An apple taken with milk and honey is highly effective in uplifting mood.
     Add a handful of fresh Rose petals to a cup a boiling water. Add sugar and drink as and when a feeling of depression sets in.""",
     ),
    ("""Dermatitis""",
     """Symptoms:
     Red and raised blisters
     Rashes
     Skin contains fluid, which oozes out id blisters break
     Ulceration""",
     """Common Types:
     Atopic Dermatitis
     Contact Dermatitis
     Stasis Dermatitis
     Discoid Eczema""",
     """Home Remedies:
     Drink Adequate water
     Aloe Vera can be consumed as well as applied topically.
     Turmeric is recommended for skin conditions for its anti-inflammatory and anit-bacterial properties""",
     ),
    ("""Diabetes""",
     """""",
     """Common Causes:
     Insulin deficiency
     High cholesterol
     Rarely due to pacreatitis""",
     """Home Remedies:
     Basil leaves are packed with antioxidants that relieve oxidative stess and have essential oils that help in lowering blood sugar levels in the body.
     Indian Blackberry is considered to be an effective medicine for treating diabetes.
     Drink a cup of green tea on an empty stomach daily in the morning before your breakfast""",
     ),
    ("""Diarrhoea""",
     """""",
     """Common causes:
     Infection caused by virus or bacteria.
     Infected foods.
     Drinking too much alcohol.
     Side effects from some medicines.""",
     """Home Remedies:
     Mash a ripe banana. Mix with 1 tsp of tamarind pulp and a pinch of salt. Take twice a day.
     A tsp of date paste mixed with 1 tsp honey. To be taken 4-5 times a day.
     Have 1 cup of fresh Pomegranate juice 3-4 times a day.""",
     ),
    ("""Dry_Skin""",
     """""",
     """Common Causes:
     Weather
     Bathing frequently
     Hypothyroidism
     High Blood Glucose""",
     """Home Remedies:
     Use of fragrance-free oils such as petroleum jelly, mineral oil provide protection from dry skin temporarily.
     A daily does of 100mg Vitamin B-Complex.
     Aloe Vera gel""",
     ),
    ("""Earache""",
     """""",
     """Common Causes:
     Blockage in ear tube
     Damage to ear drum
     Sinusitis
     Pharyngitis
     """,
     """Home Remedies:
     Grind a few basil leaves and extract some juice. Apply 2 drop inside the ear.
     Drip 2 or 3 drops of warm mustard oil into the infected ear and allow it to remain there.
     Include foods in your diet that are rich in Vitamin C such lemons, oranges, guavas, strawberries and papayas to reduce the earache.""",
     ),
    ("""Eczema""",
     """""",
     """Common Causes:
     Dust mites and pollen.
     Soaps or detergents.
     Specific allergies to foods.""",
     """Home Remedies:
     Coconut oil can be used as a natural moisturizer.
     Nutmeg against a smooth stone with a few drops of water. Make a smooth paste. Apply.
     Bathing plays an important role in eczema treatment, as it helps moisturize the skin.""",
     ),
    ("""Fatigue""",
     """Types of Fatigue:
     Central fatigue: The rate of muscle activation controlled by the central nervous system is impaired.
     Peripheral fatigue: The rate of muscle activation controlled by other peripheral mechanisms is impaired.""",
     """Common Causes:
     Abnormal functioning of the immune system.
     Lack of sleep, irregular work shifts, pregnancy, sleep apnea, Alcohol or drug abuse.
     Medications such as anti-histamines, anti-depressants, sedatives""",
     """Home Remedies:
     Drink lot of water. One must drink at least 8 glasses of water a day. It is not sufficient to wait till you are thirsty to drink water.
     Have magnesium, vitamin E, vitamin C, and calcium supplements
     In order to deal with stress and anxiety, techniques such as deep breathing, meditation, and yoga are recommended.""",
     ),
    ("""Fever""",
     """Symptoms:
     Some symptoms during a fever are headache, sweating, shivering, burning eyes, muscle ache, dehydration, loss of appetite, body pain and weakness.
     A high fever in the range of 103 °F to 106 °F can also cause symptoms such as irritability, hallucinations and convulsions.""",
     """Common Causes:
     Sunburn, cold & flu, infection in the ear or throat can cause fever.
     Fever can also be present due to malaria, typhoid or hypothermia.
     Fever may be present during infection of the urinary tract, meningitis, measles, chickenpox, typhus, hyperthyroidism and pneumonia.
     Essentially there may be any number of reasons that can cause high body temperature. On certain occasions, the cause of fever is difficult to determine""",
     """Home Remedies:
     Ginger tea reduces inflammations and infections, thereby, reducing the fever.
     Capsaicin found in cayenne pepper induces sweating and improves blood circulation. This is why the use of cayenne pepper is one of the most useful home remedies for fever.
     Drinking lemon juice in lukewarm water can ward off the fever.""",
     )
]

add_many(stuff)
