{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# The Sparks Foundation: Task 1"
    "# DONE BY: AVISHEK DAS"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task-1 : To Explore Supervised Machine Learning using Student_scores.csv dataset"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Importing the required Library packages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Importing the Dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(r'C:\\Users\\Admin\\Desktop\\student_scores.csv')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# The First Five Rows of the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.5</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5.1</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.2</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8.5</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Hours  Scores\n",
       "0    2.5      21\n",
       "1    5.1      47\n",
       "2    3.2      27\n",
       "3    8.5      75\n",
       "4    3.5      30"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Random five rows from the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>7.7</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.2</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>3.3</td>\n",
       "      <td>42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1.5</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>2.7</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Hours  Scores\n",
       "10    7.7      85\n",
       "2     3.2      27\n",
       "13    3.3      42\n",
       "5     1.5      20\n",
       "20    2.7      30"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sample(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Structure and aspects of the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 25 entries, 0 to 24\n",
      "Data columns (total 2 columns):\n",
      " #   Column  Non-Null Count  Dtype  \n",
      "---  ------  --------------  -----  \n",
      " 0   Hours   25 non-null     float64\n",
      " 1   Scores  25 non-null     int64  \n",
      "dtypes: float64(1), int64(1)\n",
      "memory usage: 528.0 bytes\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(df.info())             #full summary of the dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "           Hours     Scores\n",
      "count  25.000000  25.000000\n",
      "mean    5.012000  51.480000\n",
      "std     2.525094  25.286887\n",
      "min     1.100000  17.000000\n",
      "25%     2.700000  30.000000\n",
      "50%     4.800000  47.000000\n",
      "75%     7.400000  75.000000\n",
      "max     9.200000  95.000000\n"
     ]
    }
   ],
   "source": [
    "print(df.describe())    #statistical details of the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(25, 2)\n"
     ]
    }
   ],
   "source": [
    "print(df.shape)      #shape of dataset\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# The data has to be checked for null values & the number of null values in each column has to be counted."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Hours     0\n",
       "Scores    0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "total number of null values =  0\n"
     ]
    }
   ],
   "source": [
    "print(\"total number of null values = \",df.isnull().sum().sum())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Representation through BoxPlot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.boxplot(df['Hours'])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.boxplot(df['Scores'])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.boxplot(df)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Representing through a ScatterPlot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1152x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig,ax = plt.subplots(figsize=(16,8))\n",
    "ax.scatter(df['Hours'],df['Scores'])            #Plotting the distribution of scores\n",
    "plt.title('Hours vs Scores') \n",
    "ax.set_ylabel('Scores')\n",
    "ax.set_xlabel('Hours')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data visualization for better interpretation of the dataset "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x2c09dd30130>"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Hours',y='Scores',data=df,kind='violin')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x2c09bce9d00>"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x='Hours',y='Scores',data=df,kind='boxen')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x2c09bc956a0>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 6 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(df)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Preparing the Data for analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[2.5]\n",
      " [5.1]\n",
      " [3.2]\n",
      " [8.5]\n",
      " [3.5]\n",
      " [1.5]\n",
      " [9.2]\n",
      " [5.5]\n",
      " [8.3]\n",
      " [2.7]\n",
      " [7.7]\n",
      " [5.9]\n",
      " [4.5]\n",
      " [3.3]\n",
      " [1.1]\n",
      " [8.9]\n",
      " [2.5]\n",
      " [1.9]\n",
      " [6.1]\n",
      " [7.4]\n",
      " [2.7]\n",
      " [4.8]\n",
      " [3.8]\n",
      " [6.9]\n",
      " [7.8]]\n",
      "[21 47 27 75 30 20 88 60 81 25 85 62 41 42 17 95 30 24 67 69 30 54 35 76\n",
      " 86]\n"
     ]
    }
   ],
   "source": [
    "X = df.iloc[:,:-1].values\n",
    "Y = df.iloc[:,1].values\n",
    "print(X)\n",
    "print(Y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Diving the dataset into training and testing data "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train,X_test,Y_train,Y_test = train_test_split(X,Y,random_state = 0,test_size=0.2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Training the Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training successfully completed\n"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "linreg=LinearRegression()\n",
    "linreg.fit(X_train,Y_train)      #Fit the training dataset\n",
    "print(\"Training successfully completed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#plotting the REGRESSION LINE---\n",
    "Y0 = linreg.intercept_ + linreg.coef_*X_train\n",
    "\n",
    "#plotting on train data\n",
    "plt.scatter(X_train,Y_train,color='red',marker='+')\n",
    "plt.plot(X_train,Y0,color='blue')\n",
    "plt.xlabel(\"Hours\",fontsize=15)\n",
    "plt.ylabel(\"Scores\",fontsize=15)\n",
    "plt.title(\"Regression line(Train set)\",fontsize=10)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Comparing the Actual score with our Predicted Scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[16.88414476 33.73226078 75.357018   26.79480124 60.49103328]\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Actual</th>\n",
       "      <th>Result</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>20</td>\n",
       "      <td>16.884145</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>27</td>\n",
       "      <td>33.732261</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>69</td>\n",
       "      <td>75.357018</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>30</td>\n",
       "      <td>26.794801</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>62</td>\n",
       "      <td>60.491033</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Actual     Result\n",
       "0      20  16.884145\n",
       "1      27  33.732261\n",
       "2      69  75.357018\n",
       "3      30  26.794801\n",
       "4      62  60.491033"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Y_pred=linreg.predict(X_test)    #Predicting the Scores for test data\n",
    "print(Y_pred)\n",
    "Y_test1 = list(Y_test)\n",
    "prediction=list(Y_pred)\n",
    "df_compare = pd.DataFrame({ 'Actual':Y_test1,'Result':prediction})\n",
    "df_compare"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# ACCURACY OF THE MODEL"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.9454906892105355"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn import metrics\n",
    "metrics.r2_score(Y_test,Y_pred)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Predicting the score using regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "predicted score for a student studying 9.25 hours in a day : [93.69173249]\n"
     ]
    }
   ],
   "source": [
    "Prediction_score = linreg.predict([[9.25]])\n",
    "print(\"predicted score for a student studying 9.25 hours in a day :\",Prediction_score)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Conclusion"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# From the above result we can say that if a studied for 9.25 hours in a day then student will secured 93.69 MARKS"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Tasks 1 Completed"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Thank You"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
