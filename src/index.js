import './style.css';
import { project } from './project';
import './dom.js';
import { saveProjects, loadProjects } from './storage';

const projects = loadProjects(project);

function addProjectsButton() {
    const addButton = document.getElementById('addButton');
    const titleInput = document.getElementById('projectTitleInput');

    addButton.addEventListener('click', () => {
        const projectTitle = titleInput.value.trim();
        if (projectTitle === '') return;

        const newProject = new project(projectTitle);
        projects.push(newProject);

        saveProjects(projects); // Persist

        renderProjects();
        titleInput.value = '';
    });
}

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
}

function renderTodos(project) {
    const todoList = document.getElementById('todoList');
    todoList.innerHTML = '';
    project.todos.forEach((todo) => {
        const todoItem = document.createElement('div');
        todoItem.textContent = todo;
        todoList.appendChild(todoItem);
    });
}

renderProjects();
addProjectsButton();
