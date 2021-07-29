FROM alpine:latest

ARG EnvironmentStage

RUN mkdir /Workspace
WORKDIR /Workspace

RUN apk --no-cache add --update git bash

RUN git clone --single-branch --branch development git://github.com/anionDev/ScriptCollection.git
RUN chmod -R +x ./ScriptCollection/Other

RUN ./ScriptCollection/Other/ServerMaintenance/Alpine/Anonymous/TorInstall.sh

RUN ./ScriptCollection/Other/ServerMaintenance/Alpine/Common/CreateUser.sh "user" "/userhome" "false" "" "false" "false"

COPY Utilities/EntryPointScript.sh /userhome/EntryPointScript.sh
RUN chmod +x /userhome/EntryPointScript.sh

RUN mkdir -p /userhome
RUN chown -R user:1000 /userhome

RUN ./ScriptCollection/Other/ServerMaintenance/Alpine/Common/ConfigureSystem.sh "$EnvironmentStage" "/Workspace/ScriptCollection" "" "/Workspace"

USER user
WORKDIR /userhome

ENTRYPOINT ["/userhome/EntryPointScript.sh"]
