FROM debian:stable-slim
RUN apt-get -y update -qq
RUN apt-get -y install git
RUN mkdir /Workspace
WORKDIR /Workspace

RUN git clone --single-branch --branch development git://github.com/anionDev/ScriptCollection.git
RUN chmod -R +x ScriptCollection/Other
RUN /Workspace/ScriptCollection/Other/ServerMaintenance/Common/AptUpdate.sh
RUN /Workspace/ScriptCollection/Other/ServerMaintenance/Anonymous/TorInstall.sh

RUN rm -rf /Workspace/ScriptCollection
FROM debian:stable-slim
RUN apt-get -y update -qq
RUN apt-get -y install git
RUN mkdir /Workspace
WORKDIR /Workspace

RUN git clone --single-branch --branch development git://github.com/anionDev/ScriptCollection.git
RUN chmod -R +x ScriptCollection/Other
RUN /Workspace/ScriptCollection/Other/ServerMaintenance/Common/AptUpdate.sh
RUN /Workspace/ScriptCollection/Other/ServerMaintenance/Anonymous/TorInstall.sh

RUN rm -rf /Workspace/ScriptCollection
ENTRYPOINT ["tor"]
