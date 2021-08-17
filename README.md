## API_test
**1) Install the requirements:**

    pip install -r requirements.txt
\
**2) Run the server:**

    uvicorn main:app --reload
\
**3) To make predictions:**
Send a POST request to **localhost:8000/predict** with a JSON in the body of the style:

    {"DaysRegistered":[10,3500],  "Income":[1000.2,93200.32],  "Recency":[1,22],  "AcceptedCmpAll":[2,5],  "MntTotal":[100,1900]}
   - "DaysRegistered": Number of days that the user has been registered. Calculated from "Dt_Customer"".
   - "Income": Customer's yearly household income.
   - "Recency": Numbers of days since the last purchase.
   - "AcceptedCmpAll": Number of accepted campaigns. Calculated as "AcceptedCmp1" + "AcceptedCmp2" + "AcceptedCmp3" + "AcceptedCmp4" + "AcceptedCmp5".
   - "MntTotal": Total amount spent in the last 2 years. Calculated as "MntFishProducts" + "MntFruits" + "MntMeatProducts" + "MntSweetProducts" + "MntWines" + "MntGoldProds".
   
   Response:

    {"prediction":{"DaysRegistered":{"0":10,"1":3500},"Income":{"0":1000.2,"1":93200.32},"Recency":{"0":1,"1":22},"AcceptedCmpAll":{"0":2,"1":5},"MntTotal":{"0":100,"1":1900},"prediction":{"0":0,"1":1}}}

A postman collection is included in the repository.

\
   **4) To make clustering:**
Send a POST request to **localhost:8000/cluster** with a JSON in the body of the style:

    {"DaysRegistered":[10,3500],  "Income":[1000.2,93200.32],  "Recency":[1,22],  "AcceptedCmpAll":[4,5],  "MntTotal":[1800,1900]}
 
   - "DaysRegistered": Number of days that the user has been registered. Calculated from "Dt_Customer"".
   - "Income": Customer's yearly household income.
   - "Recency": Numbers of days since the last purchase.
   - "AcceptedCmpAll": Number of accepted campaigns. Calculated as "AcceptedCmp1" + "AcceptedCmp2" + "AcceptedCmp3" + "AcceptedCmp4" + "AcceptedCmp5".
   - "MntTotal": Total amount spent in the last 2 years. Calculated as "MntFishProducts" + "MntFruits" + "MntMeatProducts" + "MntSweetProducts" + "MntWines" + "MntGoldProds".

Response:

    {"clustering":{"Income":{"0":1000.2,"1":93200.32},"Recency":{"0":1,"1":22},"DaysRegistered":{"0":10,"1":3500},"AcceptedCmpAll":{"0":4,"1":5},"MntTotal":{"0":1800,"1":1900},"principal_feature1":{"0":2.5899670138988293,"1":6.97560806796419},"principal_feature2":{"0":12.737711334271983,"1":-0.021315033449152202},"cluster":{"0":3,"1":4}}}
A postman collection is included in the repository.

\
**5) Replication of the exploratory and training process:**
To replicate the exploratory, clustering and classification process, all the boxes of the notebook called **"final_notebook.ipynb"** included in the folder **"replicate"** of the repository must be executed. The notebook is also available at the following link: [Notebook in Google Colab](https://drive.google.com/file/d/1AQStFhrj2lDsV9Ts3sZWp77alYI7uLLQ/view?usp=sharing)