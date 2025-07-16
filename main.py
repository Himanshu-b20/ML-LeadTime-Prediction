import streamlit as st
from ui_data import product_group_list, tail_type_list, supplier_list, legacy_tail_type_list, legacy_supplier_list, \
    change_type_list, order_comp_list, advisory_note_list, task_list
from prediction_helper import predict_lt

st.set_page_config(page_title="Lead Time Prediction", page_icon="📈")
st.title("📊 Lead Time Predictor")

row1 = st.columns(2)
row2 = st.columns(2)
row3 = st.columns(2)
row4 = st.columns(2)
row5 = st.columns(2)

with row1[0]:
    task_name = st.selectbox('Task Name', sorted(task_list))
with row1[1]:
    country = st.selectbox('Country', ['UK', 'Global'])

with row2[0]:
    product_group = st.selectbox('Product Group', sorted([pro.replace('"','')  for pro in product_group_list]))
with row2[1]:
    tail_type = st.selectbox('Tail Type',sorted([item.replace('"','')  for item in tail_type_list]))

with row3[0]:
    supplier = st.selectbox('Supplier', sorted([item.replace('"','')  for item in supplier_list]))
with row3[1]:
    legacy_tail_type = st.selectbox('Legacy Tail Type', sorted([item.replace('"','')  for item in legacy_tail_type_list]))

with row4[0]:
    legacy_supplier = st.selectbox('Legacy Supplier', sorted([item.replace('"','')  for item in legacy_supplier_list]) )
with row4[1]:
    change_type = st.selectbox('Change Type', sorted([item.replace('"','')  for item in change_type_list]))

with row5[0]:
    order_complexity = st.selectbox('Order Complexity', sorted([item.replace('"','')  for item in order_comp_list]))
with row5[1]:
    advisory_note = st.selectbox('Advisory Note', sorted(advisory_note_list))

if st.button("Predict Lead Time"):

    data = ' '.join([
        task_name,
        country,
        product_group,
        tail_type,
        supplier,
        legacy_tail_type,
        legacy_supplier,
        change_type,
        order_complexity,
        advisory_note
    ])
    print(data)
    time = predict_lt(data) + 1
    st.markdown(
        f"<div style='background-color:#2E86C1; color: #FFFFFF; padding: 10px; border-radius: 8px; font-size: 18px; font-weight: bold;'>"
        f"✅ Task Creation + {str(time[0])} days"
        f"</div>",
        unsafe_allow_html=True
    )
