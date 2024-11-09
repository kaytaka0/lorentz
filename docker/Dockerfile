FROM manimcommunity/manim

RUN curl -sSL https://install.python-poetry.org | python3 -

USER root
RUN apt update
RUN apt install -y sudo git
RUN gpasswd -a $USER sudo
RUN echo "$USER  ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER ${USER}
RUN cp /home/manimuser/.bashrc /manim/.bashrc
CMD ["/bin/bash"]