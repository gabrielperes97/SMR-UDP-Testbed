# SMR-UDP Testbed

## Container
Utilizado uma imagem modificada baseada na imagem do [OpenSpliceDocker 6.4](https://hub.docker.com/r/gabrielperes97/opensplice) e no [ContainerNet](https://hub.docker.com/r/gabrielperes97/contextnetdocker), uma versão do mininet baseada em containers.

## Mininet
Especifiquei uma topologia para o mininet baseada nas especificações de rede 3g usadas pelo emulador do android (AVD).
Defini para o script python já iniciar os testes automaticamente.

## ShellScript
Utilizei um shellscript para rodar o script python em cada uma das opções de teste definidas. Os resultados são armazenados em CSV.