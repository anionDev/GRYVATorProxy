FROM debian:stable-slim
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update
RUN apt-get -y install git
RUN mkdir /Workspace
WORKDIR /Workspace
RUN git clone --single-branch --branch master git://github.com/anionDev/ScriptCollection.git
RUN chmod -R +x ./ScriptCollection/Other

RUN /Workspace/ScriptCollection/Other/ServerMaintenance/Anonymous/TorInstall.sh

# TODO hardening

COPY Utilities/EntryPointScript.sh /EntryPointScript.sh
RUN chmod +x /EntryPointScript.sh
ENTRYPOINT ["/EntryPointScript.sh"]
