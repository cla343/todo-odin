export function saveProjects(projects) {
    localStorage.setItem('projects', JSON.stringify(projects));
}

export function loadProjects(ProjectClass) {
    const saved = localStorage.getItem('projects');
    const projects = [];

    if (saved) {
        const parsed = JSON.parse(saved);
        parsed.forEach(p => {
            const project = new ProjectClass(p.title);
            project.todos = p.todos || [];
            projects.push(project);
        });
    }

    return projects;
}
