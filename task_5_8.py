def flip_str(s):
    s1 = s[::-1]
    return s1

st = 'Привет меня зовут так-то, как твои дела'
lis_st = st.split()
st_result = ''
for element in lis_st:
    st_result = st_result + ' ' + flip_str(element)
print(st_result)

