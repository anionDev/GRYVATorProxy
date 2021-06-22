FROM debian:stable-slim
RUN apt-get -y update -qq
RUN apt-get -y install git
RUN mkdir /Workspace
WORKDIR /Workspace

RUN git clone --single-branch --branch development git://github.com/anionDev/ScriptCollection.git
RUN chmod -R +x ScriptCollection/Other
RUN /Workspace/ScriptCollection/Other/ServerMaintenance/Common/AptUpdate.sh
RUN /Workspace/ScriptCollection/Other/ServerMaintenance/Anonymous/TorInstall.sh

# see https://github.com/htrgouvea/nipe
RUN apt-get -y install perl
RUN git clone git://github.com/htrgouvea/nipe.git
WORKDIR /Workspace/nipe
RUN yes | perl -MCPAN -e 'install Try::Tiny'
RUN yes | perl -MCPAN -e 'install Config::Simple'
RUN cpan JSON
RUN nipe.pl install

# TODO setup using nipe as proxy

RUN ScriptCollection/Other/ServerMaintenance/Common/Hardening.sh
RUN rm -rf /Workspace/ScriptCollection
USER user
