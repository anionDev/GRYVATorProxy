FROM debian:stable-slim
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update
RUN apt-get -y install git
RUN mkdir /Workspace
WORKDIR /Workspace
RUN git clone --single-branch --branch development git://github.com/anionDev/ScriptCollection.git
RUN chmod -R +x ./ScriptCollection/Other

RUN /Workspace/ScriptCollection/Other/ServerMaintenance/Anonymous/TorInstall.sh

# USER debian-tor
# RUN whoami
# RUN rm -rf /Workspace/ScriptCollection
# RUN ls -la /var/lib/tor
# USER debian-tor
# RUN chown -R root:root /var/lib/tor

COPY Utilities/EntryPointScript.sh /EntryPointScript.sh
RUN chmod +x /EntryPointScript.sh
ENTRYPOINT ["/EntryPointScript.sh"]
