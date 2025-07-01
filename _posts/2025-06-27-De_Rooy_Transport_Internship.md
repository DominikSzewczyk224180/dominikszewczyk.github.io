---
layout: post
title: Intelligent Pickup Prediction System for De Rooy Transport
subtitle: A Machine Learning Solution for Logistics Optimization
gh-repo: DominikSzewczyk224180/Projects-2024-2025
gh-badge: [star, fork, follow]
tags: [Machine Learning, Data Science, Predictive Analytics, Logistics Optimization, Streamlit, Route Planning]
thumbnail-img: /assets/img/derooy_project_thumbnail.pngcomments: truemathjax: falseauthor: Dominik Szewczyk
categories: projects
---
{: .box-success}This project, developed during my internship at De Rooy Transport, introduced an AI-driven system to predict unexpected pickups, optimizing logistics efficiency and sustainability. By leveraging machine learning models and a user-friendly Streamlit dashboard, the system forecasts pickup occurrences, locations, sizes, quantities, and insertion times, reducing operational costs and emissions.

**Project Duration:** January 2025 - June 2025  

## 💡 Project Summary  
Collaborating with De Rooy Transport, I designed a predictive system to address the challenge of unexpected pickups, which account for over 82% of daily assignments. The system uses a multi-model machine learning pipeline to forecast pickup details with high accuracy, integrating seamlessly with PTV route planning software. A Streamlit dashboard enables planners to upload data, analyze trends, evaluate models, and generate forecasts, achieving significant savings in distance, costs, and CO2 emissions.

## 🖼️ Image Inpainting & Semantic Segmentation  

Pickup Occurrence Prediction: Developed a Keras Sequential model to predict pickup occurrences across 5km × 5km grid cells in the Netherlands, achieving 90.2% accuracy, 88.9% precision, and 86.5% F1-score.  
Exact Location Prediction: Utilized a RandomForestClassifier to predict precise pickup locations within grid cells, achieving a mean distance error of 18 meters and 100% of predictions within 1 km.  
Size and Quantity Prediction: Employed RandomForestRegressor models to estimate loading meters (MAE: 5.39 meters) and shipment units (MAE: 14.11 units), providing actionable approximations for route planning.  
Insertion Time Prediction: Implemented an XGBRegressor to forecast pickup insertion times, reducing mean absolute error to 1 hour 7 minutes, enhancing schedule integration.  
Feature Engineering: Engineered spatial, temporal, and holiday features from historical data, improving model robustness and accuracy during peak periods.

## 🖥️ Streamlit Dashboard Development

Built a user-friendly Streamlit dashboard hosted on a secure server, enabling non-technical planners to:  
Upload & Analyze Data: Drag-and-drop CSV uploads with exploratory data analysis (EDA) visualizations for pickup trends and outliers.  
Train & Evaluate Models: Configure and assess model performance with intuitive metrics and interactive maps.  
Forecast Pickups: Generate predictions for future dates, exportable as CSV for PTV integration, with summary metrics like confidence scores.


Ensured accessibility with clear interfaces and actionable insights, streamlining logistics planning.

## 📈 Outcomes & Impact

Operational Efficiency: Sample tests on May 26 and May 28, 2025, demonstrated savings of 727.46 km and 485.29 km, respectively, alongside reductions in fuel costs (€181.86 and €121.32), CO2 emissions (945.70 kg and 630.88 kg), and planning time (7.27 and 4.85 hours).  
Scalability: Designed for implementation in August 2025, the system integrates predicted pickups into daily routes, dynamically updating with actual pickups.  
Sustainability: Reduced emissions align with De Rooy’s environmental goals, with potential daily savings of up to 1500 km.  
Future Potential: Recommended short-term expansion to predict deliveries and long-term deployment across Network Benelux for regional optimization.

## 💬 Recommendation from De Rooy

{: .box-info}
> “From our side, it was a fun and valuable experience working with Dominik. He didn’t just put in the work – he showed that he understands what matters: practical value, smart use of data, and a fresh perspective on how things can be improved. We’re very happy with the result and his contribution to De Rooy. Dominik can be proud of what he has created. We certainly are.
>
> He wasn’t just a smart guy, but also a great colleague – always prepared, always sharp, and with a good sense of humor. We won’t forget him, and if we need some clever AI support or a sharp eye on our processes in the future, we’ll definitely keep him in mind.
>
> I wish him all the best in whatever comes next – and hopefully, our paths will cross again someday.”
>
> — **Nanko Hensen**, De Rooy Transport & Logistics


## 📹 Project Presentation

Watch the Project Presentation on YouTube: https://youtu.be/IJ8YJA15uSc

## 🛠 Skills

- Machine Learning (Keras, RandomForest, XGBoost)  
- Data Science & Feature Engineering  
- Predictive Analytics  
- Logistics Optimization  
- Streamlit Dashboard Development  
- Python  
- Data Visualization  
- Route Planning Integration  
- Exploratory Data Analysis (EDA)
