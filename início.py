import flet as ft

def main(page: ft.Page):
   
       

    def a(r):
      num = int(textoa.value) + int(textob.value) 
      mensagem.value = f'Deu {num}'       
      page.update()   
    def b(r):
      num = int(textoa.value) - int(textob.value)
      mensagem.value = f'Deu {num}'       
      page.update() 
    def c(r):
      if int(textob.value) == 0:
        mensagem.value = f'Inválido' 
      else:            
        num = int(textoa.value) / int(textob.value)
        mensagem.value = f'Deu {num}'       
      page.update()
    def d(r):
      num = int(textoa.value) * int(textob.value) 
      mensagem.value = f'Deu {num}'        
      page.update()
    
    mensagem = ft.Text('', size = 25, text_align=ft.TextAlign.CENTER)           
    textoa = ft.TextField('1º numero')
    textob = ft.TextField('2º número')    

    som = ft.Button('+', on_click = a) 
    sub = ft.Button('-', on_click = b) 
    div = ft.Button('/', on_click = c) 
    mul = ft.Button('*', on_click = d) 

    container = ft.Container(
      content = ft.Row([
      
        textoa,
        
        ft.Column([
        
              som,
              sub,
              div,
              mul           

        ]), 
        
        textob,            
        mensagem                       
      ])
    )

    page.add(container)
    
ft.run(main)
