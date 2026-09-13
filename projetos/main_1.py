import flet as ft


def main(page: ft.Page):

    titulo = ft.Text(
        "Guilherme Lucas",
        size=50,
        weight=ft.FontWeight.BOLD
    )

    subtitulo = ft.Text(
        "Técnico em Informática - Turma 2º Ano (IFNMG). "
        '''
        "O Python é muito interessante, mas não mais que dormir"''',
        size=30, color = "#ab13ff",
        text_align=ft.TextAlign.CENTER
    )

    imagem = ft.Image(
        src="https://i.pinimg.com/736x/cb/06/0a/cb060af81211484956a476b02caf80c6.jpg",
        height=400
    )

    botao_a = ft.ElevatedButton("Perfil")

    botao_b = ft.OutlinedButton("Projetos")

    botoes = ft.Row(
        [
            botao_a,
            botao_b
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    coluna = ft.Column(
        [
            titulo,
            subtitulo,
            imagem,
            botoes
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    container = ft.Container(
        content=coluna,
       
    )

    page.add(container)


if __name__ == "__main__":
    ft.run(main)

