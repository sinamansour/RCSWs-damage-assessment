from joblib import load
input_string = input('****************************\n****************************\n\
Enter elements of a list separated by space with this order:\n[(Aspect ratio),(Boundry Condition),(X_1),(X_1),(Crushing)]\n\n\
For exaple:\n0.54 0 1.0098 0.8325 0.0\n')
print("\n")
user_list = input_string.split()
# print list
print('list: ', user_list)
# convert each item to float type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = float(user_list[i])
clf = load('filename.joblib')
predict=clf.predict([user_list])
if predict==1:
    result='IO'
elif predict==2:
    result='LS'
elif predict==0:
    result='CP'
print('****************************')
print('Performance state of the RCSW is:')
print('***\n**\n*')
print(result)
print('*\n**\n***')
print('****************************')
input('Press Enter bottom')