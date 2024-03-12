import flet as ft 

def main(page: ft.Page) -> None:
    page.title="Login"    
    page.vertical_alignment="center"
    page.theme_mode="light"
    page.window_width=400
    page.window_height=400
    page.window_resizable=False
    
    username = ft.TextField(label="Username", text_align=ft.TextAlign.LEFT, width=200)
    password = ft.TextField(label="Password", text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkboxsignup = ft.Checkbox(label="I agree to stuff", value=False)
    button_submit = ft.ElevatedButton(text='Sign up', width=200, disabled=True)
        
    def validate(e) -> None:
        if all([username.value, password.value, checkboxsignup.value]):
            button_submit.disabled=False
        else:
            button_submit.disabled=True
        page.update()
        
    def submit(e) -> None:
        print('Username:', username.value)
        print('Password:', password.value)
        page.clean()
        page.add(
            ft.Row(
                controls=[
                    ft.Text(value=f'Welcome: {username.value}!', width=20), 
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        
    checkboxsignup.on_change=validate
    username.on_change=validate
    password.on_change=validate
    button_submit.onclick=submit
    
    page.add(
        ft.Row(
            controls=[
                ft.Column(
                    [username,
                     password,
                     checkboxsignup,
                     button_submit]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)