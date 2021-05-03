Problema a ser resolvido:


A kiki está com muitas demandas, e não está conseguindo mais fazer as entregas com a sua vassoura, recebendo seus pedidos pelo telefone da Pagaria.
Precisamos criar uma aplicação que ajude os clientes da kiki, realizarem solicitações para que ela busque seus pacotes e os entregue.


Jornada do usuário:

O usuário deve conseguir se conectar na plataforma da bruxinha, a partir de um cadastro / login e, iniciar seu pedido de delivery.

Seu pedido irá conter o endereço de busca + endereço de entrega, peso estimado do pacote (para que a bruxinha consiga se preparar melhor para a viagem)
Também há em uma entrega, a data e um horário estimado para a entrega.




docker-compose:
- kibana
- elastic
- apm
- postgres
- redis

Levantar o serviço localmente:

Celery Parameters:
worker -A src.celery_main.celery_app -l info -P gevent -n kikis-delivery-service-worker@%n --autoscale=1,1 -Q kikis-delivery-service

Gunicorn Parameters:
-c ./src/gunicorn.py src.app:app


-> Buscar todos deliveries por status
-> Biscar todos deliveries de uma pessoa
->