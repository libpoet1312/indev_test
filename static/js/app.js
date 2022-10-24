$(document).ready(() => {
    responsive_menu();
});

const responsive_menu = () => {
    let menu_btn = $("#menu-btn");
    let sidebar = $("#sidebar");
    let container = $(".my-container");
    menu_btn.on('click', () => {
        sidebar.toggleClass("active-nav");
        container.toggleClass("active-cont");
    })
};
