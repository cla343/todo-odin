import './style.css';
import { project } from './project';
import './dom.js';

const projects = [];

function addProjectsButton() {
    console.log('Add button clicked'); // <-- check this logs

    const addButton = document.getElementById('addButton');
    const titleInput = document.getElementById('projectTitleInput')

    addButton.addEventListener('click', () => {
            const projectTitle = titleInput.value.trim();

            if (projectTitle === '') return;

            const newProject = new project(projectTitle);
            projects.push(newProject);
            renderProjects();

            titleInput.value = ''; 
        }
    )};

    function renderProjects() {
        const projectList = document.getElementById('projectList');
        projectList.innerHTML = '';
        projects.forEach((project, index) => {
            const projectItem = document.createElement('div');
            projectItem.textContent = project.title;
            projectItem.addEventListener('click', () => {
                renderTodos(project);
            });
            projectList.appendChild(projectItem);
        });
    };

    addProjectsButton();

    function renderTodos(project) {
        const todoList = document.getElementById('todoList');
        todoList.innerHTML = ''; // Clear previous todos
    
        project.todos.forEach((todo, index) => {
            const todoItem = document.createElement('div');
            todoItem.textContent = todo; // If todo is an object, adjust this
            todoList.appendChild(todoItem);
        });
    }
    
