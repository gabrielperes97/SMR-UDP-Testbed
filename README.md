# SMR-UDP Testbed

## Container
Utilizado uma imagem modificada baseada na imagem do [OpenSpliceDocker 6.4](https://github.com/gabrielperes97/OpenSpliceDocker) e no [ContainerNet](https://github.com/containernet/containernet), uma versão do mininet baseada em containers.

## Mininet
Especifiquei uma topologia para o mininet baseada nas especificações de rede 3g usadas pelo emulador do android (AVD).
Defini para o script python já iniciar os testes automaticamente.

## ShellScript
Utilizei um shellscript para rodar o script python em cada uma das opções de teste definidas. Os resultados são armazenados em CSV.

## O que falta
* Executar tudo com 100.000 samples.
* Documentar
* Criar os gráficos
* Colocar o container criado no github e no dockerhub
* Colocar o programa de testes no github, provavelmente aqui.