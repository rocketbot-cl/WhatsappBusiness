## How to use this module
To use this module, you must perform the following configuration:
1. __Log in__ or __register__ at https://developers.facebook.com/
2. Go to your Apps at https://developers.facebook.com/apps/
3. Create a new App. It must be a Business App. On the next page, choose the name, the administrator's email and the Business Account to which the App will be linked.
4. When creating the App, you will be redirected to the App page, which will be in Development mode. On this page, select in the Whatsapp app the __Configure__ button and then __API Configuration__. When you click Continue, you will be given a test number to send messages and up to 5 contacts that you can add to receive the test messages.
5. On the Quick Start page, click __Start using the API__. 
6. In both the development and production App, you can only send messages that include text to conversations that have been initiated by the user. If the conversation is initiated by the company, you must send templates that have been approved by META. For more information check the following link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
7. On the Getting Started page, you will see a temporary access token to use the API. This token lasts for 24 hours. If you want to use the API for a longer period of time, you must request a permanent access token (See point 12).
8. In this section you will have access to the Whatsapp test number and recipient number settings. You also have the phone number identifier. Both this data and the token will be required to connect through the module in developer mode.
9. Try to associate a recipient and send from the module the default hello_world template with the en_US language. If everything works correctly, you will receive a Whatsapp message with the text "Hello World!".
10. Once you have checked the operation, you can create your own templates that need to be approved by META and send them through the module. For more information about the templates, check the following link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
11. Once you have tested the API functionality, you will need to add a phone number of your company to be able to send messages to your customers. Click on the button in step 5 __Add phone number__ and follow the steps to create the Whatsapp Business profile. Once added, save the phone number identifier, this data will be necessary to be able to connect through the module.
12. Once you have a phone number added, it remains to configure the application to switch to productive mode and generate a permanent access token. To do this, go to the App page at https://developers.facebook.com/apps/ and select the App you created. On the App page, select the "Configure" button in the Whatsapp app and then "Basic Settings".
13. There you must provide a __Privacy Policy URL__ as mandatory and the rest of the fields as optional. At the end click on __Save changes__.
14. With everything configured, the app is ready to go to Active mode. To do this go to the top of the web and move the Development selector to Active. 
15. Get a permanent token: To do this you must have a Meta trading account. Go to https://business.facebook.com/ and in the left menu select your company, and click on the configuration wheel, then Business Settings. In the new window click on System users and add a new one.
16. Accept the message in the window that opens and then select a name for your new user. Under Role you should put Administrator.
17. When creating the user click on the __Add assets__ button. In the window that will open select Apps, then check the App you created and activate the option __Manage App__, then Save the changes.
18. When assigning the asset, click on __Generate new token__. Select your App and check all permissions from the list (They are not all required but if more integrations are added to Rocketbot in the future you will be able to use the same token). Click on __Generate token__. This will be the permanent token that you will be able to use to authenticate in the module.

---

## Como usar este m??dulo
Para utilizar este m??dulo, se debe realizar la siguiente configuraci??n:
1. __Inicia sesi??n__ o __reg??strate__ en https://developers.facebook.com/
2. Ve a tus Apps en https://developers.facebook.com/apps/
3. Crea una nueva App. Debe ser de tipo Negocio. En la p??gina siguiente, elije el nombre, el correo del administrador y la Cuenta comercial a la que se vincular?? la App.
4. Al crear la App, se te redirigir?? a la p??gina de la misma, la cual se encontrar?? en modo Desarrollo. En esta p??gina, selecciona en la app Whatsapp el bot??n __Configurar__ y luego __Configuraci??n de la API__. Al hacer click en Continuar, se te otorgar?? un n??mero de prueba para enviar mensajes y hasta 5 contactos que puedes agregar para recibir los mensajes de prueba.
5. En la p??gina de Inicio r??pido, haz click en __Empezar a usar la API__. 
6. Tanto en la App en desarrollo como en producci??n, s??lo puedes enviar mensajes que incluyen texto a conversaciones que hayan sido iniciadas por el usuario. Si la conversaci??n es iniciada por la empresa, deber??s enviar plantillas que hayan sido aprobadas por META. Para m??s informaci??n revisa el siguiente link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
7. En la p??gina de Primeros pasos, ver??s un token de acceso temporal para usar la API. Este token tiene una duraci??n de 24 horas. Si quieres usar la API por m??s tiempo, debes solicitar un token de acceso permanente (Ver punto 12).
8. En esta secci??n tendr??s acceso al n??mero de prueba de Whatsapp y a la configuraci??n de los n??meros de destinatario. Tambi??n tienes el Identificador de n??mero de tel??fono. Tanto este dato como el token ser??n necesarios para poder conectarte a trav??s del m??dulo en modo desarrollador.
9. Prueba asociar un destinatario y enviar desde el m??dulo la plantilla por defecto hello_world con el lenguaje en_US. Si todo funciona correctamente, recibir??s un mensaje de Whatsapp con el texto "Hello World!".
10. Una vez comprobado el funcionamiento, puedes crear tus propias plantillas que necesitan ser aprobadas por META y enviarlas a trav??s del m??dulo. Para m??s informaci??n sobre las plantillas, revisa el siguiente link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
11. Una vez que hayas comprobado el funcionamiento de la API, deber??s agregar un n??mero de tel??fono de tu empresa para poder enviar mensajes a tus clientes. Haz click en el bot??n del paso 5 __Agregar n??mero de tel??fono__ y sigue los pasos para crear el perfil de Whatsapp Business. Una vez agregado, guarda el Identificador de n??mero de tel??fono, este dato ser?? necesario para poder conectarte a trav??s del m??dulo.
12. Al tener un n??mero de tel??fono agregado, queda configurar la aplicaci??n para pasar al modo productivo y generar un token de acceso permanente. Para esto, debes ir a la p??gina de la App en https://developers.facebook.com/apps/ y seleccionar la App que creaste. En la p??gina de la App, selecciona en la app Whatsapp el bot??n "Configurar" y luego "Configuraci??n b??sica".
13. All?? deber??s otorgar una __URL de la Pol??tica de privacidad__ de forma obligatoria y el resto de campos de forma opcional. Al finalizar haz click en __Guardar cambios__.
14. Con todo ya configurado, la app est?? lista para pasar al modo Activo. Para ello ve hacia arriba de todo en la web y mueve el selector de Desarrollo a Activo. 
15. Obtener token permanente: Para ello debes tener una cuenta comercial de Meta. Ingresa a https://business.facebook.com/ y en el men?? de la izquierda selecciona tu empresa, y haz click en la rueda de configuraci??n, luego en Configuraci??n de negocio. En la nueva ventana haz click en Usuarios del sistema y agrega uno nuevo.
16. Acepta el mensaje de la ventana que se abre y luego selecciona un nombre para tu nuevo usuario. En Rol debes colocar Administrador.
17. Al crear el usuario haz click en el bot??n __Agregar activos__. En la ventana que se abrir?? selecciona Apps, luego marca la App que creaste y activa la opci??n __Administrar App__, luego Guarda los cambios.
18. Al asignar el activo, haz click en __Generar nuevo token__. Selecciona tu App y marca todos los permisos de la lista (No son todos necesarios pero si en un futuro se agregan m??s integraciones en Rocketbot podr??s utilizar la misma credencial). Haz click en __Generar token__. Este ser?? el token permanente que podr??s utilizar para autenticarte en el m??dulo.

---

## Como usar este m??dulo
Para utilizar este m??dulo, ?? necess??ria a seguinte configura????o:
1. __Log in__ ou __register__ em https://developers.facebook.com/
2. v?? para suas aplica????es em https://developers.facebook.com/apps/
3. Criar um novo aplicativo. Deve ser uma aplica????o comercial. Na p??gina seguinte, escolha o nome, o e-mail do administrador e a conta comercial ?? qual o aplicativo estar?? vinculado.
4. Ao criar o aplicativo, voc?? ser?? redirecionado para a p??gina do aplicativo, que estar?? no modo Desenvolvimento. Nesta p??gina, selecione o bot??o __Configure__ no aplicativo Whatsapp e depois selecione __API Configuration__. Ao clicar em Continuar, voc?? receber?? um n??mero de teste para enviar mensagens e at?? 5 contatos que voc?? pode adicionar para receber as mensagens de teste.
5. Na p??gina Quick Start, clique em __Start usando a API__. 
6. Tanto na aplica????o de desenvolvimento quanto na de produ????o, s?? ?? poss??vel enviar mensagens que incluam texto para conversas que tenham sido iniciadas pelo usu??rio. Se a conversa for iniciada pela empresa, voc?? dever?? enviar modelos que tenham sido aprovados pela META. Para mais informa????es, consulte o seguinte link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
7. Na p??gina de Primeiros Passos, voc?? ver?? um token de acesso tempor??rio para usar o API. Esta ficha tem uma dura????o de 24 horas. Se voc?? quiser usar o API por mais tempo, dever?? solicitar um token de acesso permanente (ver ponto 12).
8. Nesta se????o voc?? ter?? acesso ao n??mero de teste Whatsapp e ??s configura????es do n??mero do destinat??rio. Voc?? tamb??m tem o identificador do n??mero de telefone. Tanto isto como a ficha ser??o necess??rios para poder se conectar atrav??s do m??dulo no modo desenvolvedor.
9. Tente associar um destinat??rio e envie do m??dulo o modelo padr??o hello_world com o idioma en_US. Se tudo funcionar corretamente, voc?? receber?? uma mensagem Whatsapp com o texto "Hello World!
10. Uma vez testados, voc?? pode criar seus pr??prios modelos que precisam ser aprovados pelo META e envi??-los atrav??s do m??dulo. Para mais informa????es sobre os modelos, consulte o seguinte link: https://developers.facebook.com/docs/whatsapp/api/messages/message-templates
11. Uma vez testada a API, voc?? precisar?? adicionar um n??mero de telefone para sua empresa a fim de poder enviar mensagens a seus clientes. Clique no bot??o no passo 5 __Adicionar n??mero de telefone__ e siga os passos para criar o perfil Whatsapp Business. Uma vez adicionado, salvo o identificador do n??mero de telefone, estes dados ser??o necess??rios para poder se conectar atrav??s do m??dulo.
12. Uma vez adicionado um n??mero de telefone, voc?? precisa configurar o aplicativo para entrar no modo produtivo e gerar um token de acesso permanente. Para fazer isso, v?? para a p??gina do aplicativo em https://developers.facebook.com/apps/ e selecione o aplicativo que voc?? criou. Na p??gina do aplicativo, selecione o bot??o "Configurar" no aplicativo Whatsapp e depois "Configura????es B??sicas".
13. A?? voc?? deve fornecer um __Privacy Policy URL__ como obrigat??rio e o resto dos campos como opcional. No final clique em __Salvar mudan??as__.
14. Com tudo configurado, o aplicativo est?? pronto para ir para o modo Ativo. Para fazer isso, v?? para o topo do site e mova o seletor de Desenvolvimento para o Active. 
15. Receba uma ficha permanente: Para fazer isso, ?? necess??rio ter uma conta Meta trading. V?? para https://business.facebook.com/ e no menu ?? esquerda selecione sua empresa, e clique na roda de configura????o, depois em Business Settings. Na nova janela, clique em System Users e adicione uma nova janela.
16. Aceite a mensagem na janela que se abre e depois selecione um nome para seu novo usu??rio. Sob a fun????o voc?? deve colocar Administrator.
17. Ao criar o usu??rio, clique no bot??o __Adicionar Ativos__. Na janela que se abre selecione Apps, ent??o marque o App que voc?? criou e ative a op????o __Manage App__, depois Salve as mudan??as.
18. Ao atribuir o bem, clique em __Gerar novo token__. Selecione seu aplicativo e verifique todas as permiss??es da lista (Nem todas s??o necess??rias, mas se mais integra????es Rocketbot forem adicionadas no futuro, voc?? poder?? usar o mesmo token). Clique em __Generar ficha__. Este ser?? o s??mbolo permanente que voc?? pode usar para se autenticar no m??dulo.

