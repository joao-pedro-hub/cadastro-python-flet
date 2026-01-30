import flet as ft

def main(page:ft.Page):
    page.title='cadrasto de alunos'
    page.bgcolor= ft.Colors.BLUE

    txt_nome= ft.Text ('nome do aluno:', size=25)
    nome = ft.TextField (label='digite o nome do aluno...', text_align=ft.TextAlign.LEFT)
    txt_serie= ft.Text('serie do matriculado...', size=25)
    serie = ft.TextField (label='digite a serie do aluno exenplo: 8°,5°...', text_align=ft.TextAlign.LEFT)
    txt_cpf= ft.Text('CPF', size=25)
    cpf= ft.TextField(label='digite o CPF do aluno...', text_align=ft.TextAlign.LEFT)
    
    def dados(e):
        print(f'O aluno {nome.value} {serie.value}foi matriculado com sucesso CPF:{cpf.value}')

    btn= ft.ElevatedButton('enviar', on_click=dados)
    
    page.add(
        txt_nome,
        nome,
        txt_serie,
        serie,
        txt_cpf,
        cpf,
        btn
    )

ft.app(target=main)