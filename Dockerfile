FROM debian:stable-slim
RUN apt-get -y update
RUN apt-get -y install git
RUN mkdir /Workspace
WORKDIR /Workspace
RUN git clone git://github.com/anionDev/ScriptCollection.git
RUN chmod -R +x ScriptCollection/Other
RUN ScriptCollection/Other/ServerMaintenance/Anonymous/TorInstall.sh
RUN ScriptCollection/Other/ServerMaintenance/Common/Hardening.sh
RUN rm -rf /Workspace/ScriptCollection
USER user
# TODO