### Data
The image dataset used in this study is publicly available from [Data](https://www.ebi.ac.uk/biostudies/studies/S-BIAD419). 
The data is lung biopsy sections stained with H&E stain from healthy control pigs or pigs subjected to lipopolysaccharide (LPS), an inflammatory agent to model acute respiratory distress syndrome (ARDS), with or without mechanical ventilation (MV) or extracorporeal membrane oxygenation (ECMO), interventions which are commonly used in ARDS patients. Lung damage scores based on the Silva scoring system from five annotators were used to generate “low”, “medium” or “high” damage labels for CNN training. [Code](https://github.com/Aitslab/lunghisto) and [paper](https://www.biorxiv.org/content/10.1101/2023.05.12.540340v1.abstract) are available.


### Exploratory Data Analysis (EDA)
EDA scripts  involve tasks such as statistical analysis, cleaning image data, attaching labels to the images, dividing them into smaller tiles, and applying data augmentation techniques. These processes, along with handling different labels, build on prior [work](https://www.biorxiv.org/content/10.1101/2023.05.12.540340v1.abstract)  and are shared at [Here](https://github.com/Aitslab/lunghisto). 
