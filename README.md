<h1>Auto Escola Back-End</h1> 


<h2>[201] Criar usuário.</h2>
<h3>POST - /api/users/</h3>
<strong>Essa rota não necessita autenticação bearer token. Campos de envio para request:</strong>

<ul>
    <li><strong>username: </strong>Entrada obrigatória do tipo string e máximo 127 chars, unico.</li>
    <li><strong>email: </strong>Entrada obrigatória do tipo string email, unico.</li>
    <li><strong>password: </strong>Entrada obrigatória do tipo string.</li>
    <li><strong>first_name: </strong>Entrada obrigatória do tipo string e máximo 50 chars.</li>
    <li><strong>last_name: </strong>Entrada obrigatória do tipo string e máximo 50 chars.</li>
    <li><strong>is_employee: </strong>Entrada opcional do tipo boolean com padrão falso.</li>
</ul>

<p>Retorno esperado com status code <strong style="color:LimeGreen;font-size:14px">201</strong> para criação realizada com sucesso:</p>

<pre>
{
	"id": 1,
	"email": "diego@mail.com",
	"username": "diego",
	"first_name": "Diego",
	"last_name": "Monteiro de Carvalho",
	"is_employee": true
}
</pre>