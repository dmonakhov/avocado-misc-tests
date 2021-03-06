
PYFILES:=$(shell find * -name "*.py" -type f -print )

default: check ;

define CHECK_ONE

check-$1:
	inspekt lint $1;
	inspekt indent $1;
	inspekt style $1;
.PHONY:check-$1

fix-indent-$1:
	inspekt indent $1 || inspekt indent --fix $1 || inspekt indent $1
.PHONY:fix-indent-$1

endef

$(eval $(foreach f,$(PYFILES),$(call CHECK_ONE,$f)))
#$(warning $(foreach f,$(PYFILES),$(call CHECK_ONE,$f)))


fix-indent:  $(addprefix fix-,$(PYFILES))
.PHONY:fix-intent

check:  $(addprefix check-,$(PYFILES))
.PHONY:check
