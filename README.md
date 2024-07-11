# Heart-Abnormality-Diagnosis

### Contents:
This repository contains my implementation of the logistic regression learning algorithm to diagnose heart abnormalities based on tomography (X-ray). The data used is from the UC Irvine Machine Learning Data Repository and was collected by Lukasz Kurgan and Krzysztof Cios. Data was split into training and testing data sets, composed of 80 and 187 data vectors respectively, with each data vector contains 22 binary input features. Finally, the output class indicates (in binary) the diagnosis either as normal or abnormal. 


### Introduction: 
Despite advancements in malaria control worldwide, the disease remains an immense global health burden. In 2022, the WHO reported 247 million cases and estimated 608,000 deaths.[1] As the deadliest malaria strains (P. falciparum and P. vivax) develop resistance to antimalarial artemisinins and evasion strategies to rapid diagnostic testing, the need for an improved diagnostic solution is greater than ever.[2, 3] Traditionally, malaria diagnosis is conducted via light microscopy or rapid diagnostic testing (RDT). However, due to the large time and expertise cost of light microscopy diagnosis, RDT’s based on Histidine-rich protein II (HRP2) and pan-Plasmodium antigen lactate dehydrogenase (pLDH) are the preferred method for fast, low-cost, point-of-care diagnosis. As a result of selection pressures, P. falciparum have developed pfhrp2 deletions to evade RDT detection, resulting in false negatives and compromising surveillance efforts.[4] In order to reduce the global burden of malaria and progress towards eradication, new, accurate approaches to surveillance testing must be developed.


### Background: 
A number of image analysis and machine learning methods have been developed to automate the detection of infected cells from blood smears.[5] However, these approaches generally do not subcategorize infected cells into their stage of the malaria life cycle. The few that do subcategorize focus on the most virulent strain, P. falciparum.[6] Since the progression of malaria is highly variable (symptoms may emerge 7 days to 1 year after infection), the stage of infected cells provide important indications of disease progression which are crucial for accurate prognosis and treatment.[7] Additionally, stage-specific diagnosis would bolster our understanding of the disease evolution and accelerate the ongoing development of stage-specific drugs, vaccines, and care protocols.[8, 9,10] Considering these advantages and the current gap in scientific literature, we sought to develop an automated image analysis program to quantify and categorize P. vivax infected cells by stage from blood smears. We utilized the “P. vivax (malaria) infected human blood smears” annotated image collection from the Broad Institute, consisting of three sets of images sourced from Brazil (Stefanie Lopes), Southeast Asia (Benoit Malleret), and Penn State University (Gabriel Rangel).[11] The dataset consisted of thick and thin blood smear images totalling 1,364 (~80,000 cells), with each cell labeled as uninfected (RBC or leukocyte) or infected (gametocyte, ring, trophozoite or schizont) for validation purposes.

### Methodology: 
<div align="center">
	<img width="778" alt="MethodsFlowChart" src="https://github.com/jasmynlopez/Heart-Abnorbmality-Diagnosis/assets/141966948/a135fb9f-0901-4ed7-ad24-ad5db728adfb">
</div>


