FROM debian:stable-slim as base

ARG EnvironmentStage

RUN mkdir /Workspace
WORKDIR /Workspace

RUN apt update
RUN apt install -y git

RUN git clone --depth 1 --single-branch --branch main https://github.com/anionDev/ScriptCollection.git
RUN chmod -R +x ./ScriptCollection/OtherScripts

RUN ./ScriptCollection/OtherScripts/ServerMaintenance/Debian/Anonymous/TorInstall.sh

RUN ./ScriptCollection/OtherScripts/ServerMaintenance/Debian/Common/CreateUser.sh "user" "/Workspace/userhome" "false" "" "false" "false"

COPY ./EntryPointScript.sh /Workspace/userhome/EntryPointScript.sh
RUN chmod +x /Workspace/userhome/EntryPointScript.sh

RUN chown -R user:1000 /Workspace/userhome
RUN chown -R user:1000 /var/lib/tor

RUN /Workspace/ScriptCollection/OtherScripts/ServerMaintenance/Debian/Common/ConfigureSystem.sh "$EnvironmentStage" "/Workspace/ScriptCollection" "" "/Workspace/ScriptCollection"

RUN tor --version

FROM scratch
ARG EnvironmentStage
COPY --from=base / /
USER user
ENTRYPOINT ["/Workspace/userhome/EntryPointScript.sh"]
