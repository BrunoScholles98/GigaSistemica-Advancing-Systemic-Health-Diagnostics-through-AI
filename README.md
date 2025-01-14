# GigaSistêmica: Advancing Systemic Health Diagnostics through AI

## Overview
GigaSistêmica is a collaborative initiative between GigaCandanga and the University of Brasília (UnB), dedicated to leveraging artificial intelligence (AI) to advance diagnostic and predictive capabilities for systemic health conditions. This project focuses on integrating dental imaging, radiomic analysis, and neural networks to develop tools for early detection and efficient healthcare delivery. As part of our commitment to open science, this repository provides a central point for tracking our research progress and associated resources.

### Projects and Publications
Below is an overview of completed and ongoing projects under the GigaSistêmica initiative. The repository will be updated as new milestones are achieved.

---

### 1. Osteoporosis Screening with Panoramic Radiographs
- **Description:** This project developed an AI-based approach to identify signs of osteoporosis using dental panoramic radiographs (PR). EfficientNet-based convolutional neural networks (CNNs) were trained on PR images to classify patients into categories based on mandibular cortical morphology, focusing on "Healthy" (C1) and "Osteoporotic" (C3) conditions. The study emphasizes the integration of dental imaging with the gold-standard Dual-energy X-ray Absorptiometry (DXA) results for validation. The study demonstrated the potential for CNNs to complement DXA by automating the initial screening process, especially in settings where DXA resources are limited. Grad-CAM visualizations were used to interpret model decisions, highlighting critical regions such as the mandibular cortex.

- **Publication:**
  - Dias, B. S. S., Querrer, R., Figueiredo, P. T., Leite, A. F., de Melo, N. S., Costa, L. R., Caetano, M. F., & Farias, M. C. Q. (2025). *Osteoporosis screening: Leveraging EfficientNet with complete and cropped facial panoramic radiography imaging*. **Biomedical Signal Processing and Control**, *100*, 107031. [https://doi.org/10.1016/j.bspc.2024.107031](https://doi.org/10.1016/j.bspc.2024.107031).
- **Repository:** [GitHub Link](https://github.com/BrunoScholles98/Deep-Learning-for-Bone-Health-Classification-through-X-ray-Imaging)

![](https://i.imghippo.com/files/2vYCY1727776056.png)

---

### 2. Detection and Segmentation of Carotid Atheroma Calcification
- **Description:** This study introduced a hybrid deep learning model to detect and segment carotid atheroma calcifications (CACs) in dental panoramic radiographs (PR). The proposed method combines the efficiency of an attention mechanism with the precision of the UNet architecture. It enables the identification and segmentation of CACs by utilizing an automated two-step process, offering a reliable and practical tool for opportunistic screening in dental settings. The model facilitates the detection of potential atherosclerosis-related risks, providing an accessible, non-invasive, and cost-effective diagnostic approach.

- **Status:** Under review at *IEEE Journal of Biomedical and Health Informatics (JBHI)*.
- **Publication:**
  - Correia, I. B. M. C., Ferreira, M. V. S., Chini, C. F., Dias, B. S. S., Costa, L. R., Caetano, M. F., Leite, A. F., de Melo, N. S., & Farias, M. C. Q. (2024). *Detection and segmentation of carotid atheroma calcification in dental panoramic radiographs using a hybrid deep learning model*. Submitted to **IEEE Journal of Biomedical and Health Informatics**.
- **Repository:** Coming soon.

![](https://i.imghippo.com/files/hr1992jZI.png)

---

### 3. Radiomic signature based on cone-beam computed tomography images for evaluation of osteoporosis
- **Description:** A radiomic signature was developed based on cone-beam computed tomography (CBCT) images for the evaluation of osteoporosis. This study involved analyzing radiomorphometric indices in mandibular structures.
- **Publication:**
  - Master’s thesis abstract available: [https://sigaa.unb.br/sigaa/public/programa/noticias_desc.jsf?lc=en_US&id=907&noticia=8652785](https://sigaa.unb.br/sigaa/public/programa/noticias_desc.jsf?lc=en_US&id=907&noticia=8652785).
- **Repository:** Under development.

---

### 4. Gunshot Wounds Classification with Deep Learning
- **Description:** This project applied deep learning models to assist in forensic investigations by classifying gunshot wounds. The system is capable of distinguishing between entry and exit wounds and determining the medico-legal shooting distance (MLSD) from digital images of real forensic cases. By leveraging convolutional neural networks, the project showcases how artificial intelligence can complement forensic experts in analyzing complex cases with increased speed and precision. This initiative represents a significant step forward in integrating AI tools within forensic pathology.

- **Publication:**
  - Lira, R. Q. N., Sousa, L. G. M., Pinho, M. L. M., Lima, R. C. P. S. A., Freitas, P. G., Dias, B. S. S., Souza, A. C. B., & Leite, A. F. (2024). *Deep learning-based human gunshot wounds classification*. **International Journal of Legal Medicine**, Published 6 November 2024. [https://doi.org/10.1007/s00414-024-03355-4](https://doi.org/10.1007/s00414-024-03355-4).
- **Repository:** [GitLab Link](https://gitlab.com/lisa-unb/leguwoi)

---

### Future Directions
The GigaSistêmica project continues to evolve, with current efforts focused on:
- **Fine-tuning a Large Language Model (LLM):** Development of a multimodal system that integrates imaging and text-based data for comprehensive systemic health analysis. This project is in its early stages.
- **Enhanced Interoperability:** Integrating developed models into a unified diagnostic pipeline for public health applications.

---

### Contact
For further inquiries or collaboration opportunities, please contact me via email: [brunoscholles98@gmail.com](mailto:brunoscholles98@gmail.com) or one of the Coordinators bellow. Additionally, you can reach me via WhatsApp at +351 913 686 499.

---

### Coordinators
Our academic and research leaders include:
- [Mylène C. Q. Farias](http://www.ene.unb.br/mylene/)
- [André Ferreira Leite](http://lattes.cnpq.br/7275660736054053)
- [Nilce Santos de Melo](http://lattes.cnpq.br/4611919012909264)
- [Marco F. Caetano](https://cic.unb.br/professores/94-mfcaetano)

---

This repository reflects our ongoing commitment to transparency and collaboration in the scientific community. Contributions and feedback are always welcome.
