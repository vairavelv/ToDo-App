import streamlit as st

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>📝 To-Do List App</h1>",unsafe_allow_html=True)

# st.title("📝 To-Do List App")
st.divider()

class Todo:
    def __init__(self):
    
        if 'todo_list' not in st.session_state:
            st.session_state.todo_list = []

    def new_task(self):

        if 'task' not in st.session_state:
            st.session_state.task = ""


        st.session_state.task = st.text_input("Enter the task: ",st.session_state.task)
        if st.button('add task'):
            if st.session_state.task.strip():
                st.session_state.todo_list.append(st.session_state.task.strip())
                st.success("Task added!")
                st.session_state.task = ""
            
            else:
                st.warning("Please enter a task before adding.")
    
    def view_task(self):
        if st.button('📝view task'):
            if len(st.session_state.todo_list) == 0:
                st.warning("You dont have ToDo list yet...kindly add before view")
            else:
                for i,tasks in enumerate(st.session_state.todo_list):
                    st.write(f"{i+1}.{tasks}")
    
    def remove_task(self):
        if st.session_state.todo_list:

            Del = st.selectbox("Select the task to delete:",st.session_state.todo_list)
            if st.button('✖️remove task'):
                st.session_state.todo_list.remove(Del)
                st.write("The task Deleted successfully")
                st.session_state.action = None
        else:
            st.info("No task to remove")
    @staticmethod
    def main():

        if 'action' not in st.session_state:
            st.session_state.action = None


        to = Todo()
        bt1,bt2,bt3 = st.columns(3)
        with bt1:
            if st.button('New task'):
                st.session_state.action = "new"
        with bt2:
            if st.button('view task'):
                st.session_state.action = "view"

        with bt3:
            if st.button('Remove the existing task'):
                st.session_state.action = "remove"
        if st.session_state.action == "new":
            to.new_task()
        elif st.session_state.action == "view":
            to.view_task()
        elif st.session_state.action == "remove":
            to.remove_task()
        


c1 = Todo()

c1.main()
