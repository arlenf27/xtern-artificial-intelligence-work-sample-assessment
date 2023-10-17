# Xtern - Artificial Intelligence Work Sample Assessment 
# Author: Arlen Feng
# Last Updated 17 October 2023

## A Brief Note on this Project
I feel obligated to mention that (as a 2nd-Year CSE student) I currently have limited formal education in Artificial Intelligence and tools such as SKLearn, pandas, and Matplotlib and was largely unfamiliar with these tools upon beginning this project. Due to this, I feel that my final model may have yielded results that did not completely represent the information provided in the dataset. 

However, I made my best attempt at getting familiar with these tools and constructing a model; I believe that in the near future, I will greatly improve my knowledge in building more accuracte models and getting more familiar with computational data analysis. I also plan on taking AI/ML electives and possibly specializing in AI. In the sections below, I outline my complete thought processes regarding the steps I took in order to complete this project to the best of my ability. 

## Files
1. **ExploratoryDataAnalysis.ipynb**: A notebook that conducts brief exploratory data analysis by visualizing several general distributions
2. **Model.ipynb**: A notebook that contains the code that attempts to develop a model to predict customers' orders
3. **Model.joblib** A joblib file that saves the model for pickling
4. **XTern 2024 Artificial Intelegence Data Set - Xtern_TrainData.csv**: A CSV version of the original dataset provided
5. **CombinedDataWithEncodings.csv**: An extended version of the data set that includes the One Hot Encodings for the inputs
6. **README.md**: A text document that **contains all answers, descriptions, and explanations for this project and the other files**

## Exploratory Data Analysis
**Structure**: The Jupyter Notebook file **ExploratoryDataAnalysis.ipynb** uses Python and Matplotlib to pull data from the Artificial Intelligence Data Set (Stored here as a csv file - **XTern 2024 Artificial Intelegence Data Set - Xtern_TrainData.csv**) in order to display several distribution plots for the years, majors, universities, times, and orders. 

**Overview**: I imported each category (Year, Major, University, etc.) to a dictionary with the total counts of how often each specific category appeared in the orders. I then plotted graphical representations for the general distributions of the input data. 

**Several Preliminary Observations**: 

1. The distribution of specific orders was very even; almost every item received around 500 orders.
2. Most students who placed orders were either in their second or third year.
3. The most common majors among students were Physics, Chemistry, Biology, Mathematics, Economy, and Astronomy.
4. Most students were from either Indiana State University, Ball State University, Butler University, or IUPUI.
5. The time of the orders were usually between 11 to 14.

**Business Use Cases**: This data can be manipulated and analyzed in order to determine which categories of students were more likely to order a specific item. It can be inferred (based on preliminary observations) that some categories would not be catered or advertised too often due to the general scarcity of their demograhics (e.g. Fourth-Year Students). By tailoring orders automatically, employees would not have to maintain day-to-day operations on predicting orders; instead, the model and algorithm behind the machine would have to be continuously maintained and modified for optimal results. 

**For specific visualizations and more detailed general distributions, see ExploratoryDataAnalysis.ipynb.**

## Implications of Data Collection, Storage, and Biases
1. **Ethical Implications**: One of the most significant ethical concerns is that the privacy of students' demographic information may be misused (either by faulty programming or by data theft). The information provided by a model may also produce biases that could impact students' view of the company and/or cause controversies over selective advertisement. In addition, vast amounts of memory would be needed to store the information provided and used by the models and systems of the resulting artificial intelligence program. Due to this, more resources would have to be allocated towards designing a secure and safe technical system.
2. **Business Outcome Implications**: The main goal of a new AI modeling program (along with related applications) will be to increase revenue by selectively targetting students who are more likely to place certain orders over others. This is reflected directly by the fact that for each incorrect order, a significant source of revenue would be lost (10% Discount). However, more resources on the business side would also have to be allocated towards hiring more technical staff in order to maintain and update these new systems. It could also be reasonably inferred that extra costs will arise when the dataset (for one reason or another) undergoes drastic change, whether it is because of company relocation or a current event. All of these factors will play into the overall outcome for the business down the line. 
3. **Technical Implications**: Although frontend programming may not receive too many changes due to this AI mechanism, the backend systems that provide vital support for the business would most likely have to be completely revamped. This is so that systems would have to be managed in a way that would accurately allocate certain functions (that were previously performed manually by humans) to the new programs. Given this fact, it can be stated with considerable confidence that the applications (while seemingly providing the same role to customers) would have to be significantly modified in favor of a new, (relatively) hands-off approach.

## Building a Model
1. **All details, code, and results can be found in the file Model.ipynb.**
2. **Outline**: I decided to use SKLearn's K-Means clustering tool because the purpose of the data was to group students with the most likely orders based on their demographics. By clustering data, the eventual goal would be for a program and to accurately pull information from a model to determine clearly which students should get specific orders. A resource I found helpful for choosing the right estimator was from this SKLearn tutorial page: https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html.
3. **Details**: First, I pulled data from the CSV file and loaded data into a data frame (loadDataIntoDataFrame()). Then (due to the fact that some of the categories were represented by strings), I used One Hot Encodings (encodeData()) to assign integer values to some of the string values (e.g. [0, 1, 0, 0] in column 5 of CombinedDataWithEncodings.csv means that the student is in Year 2). I then attempted to create a K-Means model (predict()), build it, and train it based off of the dataset. Several important statistical outcomes (such as the locations of the centroids) were than printed and outputted (printResults()). Finally, I tried to use joblib to dump and save the model with the idea being that it could learn and improve from its previous findings. Although I realize that the output of the model may not have been completely accurate, I believe that there is a better way to map the encodings to the resulting categorical values, and that final plots may reflect distributions more accurately if the different centroids were more apparently separated. 

## Conclusion
Given the work required to bring a solution to maturity, I believe that creating a machine-learning model to predict orders would be a perfectly reasonable course of action. Although there may be many tasks to be done regarding specific implementations of the model (and its surrounding systems) as well as the fine-tuning of specific programs (such as those related to accurately mapping encodings to their actual representation), I believe that the potential of delegating a significant amount of work to an accurate model may outweigh all of these considerations. Employees would not have to do more work regarding specific predictions, and the chance of human errors to occur within the decision-making processes may decrease as a result of a more "hands-off" approach. Overall, with significant fine-tuning, a valuable deployable mechanism could result in much more revenue for the business processes. 