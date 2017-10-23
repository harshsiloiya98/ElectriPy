class diode_model(object):
    """A diode model implementing the `Shockley diode equation
    <http://en.wikipedia.org/wiki/Shockley_diode_equation#Shockley_diode_equation>`__.

    Currently the capacitance modeling part is missing.

    The principal parameters are:

    +---------------+-------------------+-----------------------------------+
    | *Parameter*   | *Default value*   | *Description*                     |
    +===============+===================+===================================+
    | IS            | 1e-14 A           | Specific current                  |
    +---------------+-------------------+-----------------------------------+
    | N             | 1.0               | Emission coefficient              |
    +---------------+-------------------+-----------------------------------+
    | ISR           | 0.0 A             | Recombination current             |
    +---------------+-------------------+-----------------------------------+
    | NR            | 2.0               | Recombination coefficient         |
    +---------------+-------------------+-----------------------------------+
    | RS            | 0.0 ohm           | Series resistance per unit area   |
    +---------------+-------------------+-----------------------------------+

    please refer to a textbook description of the Shockley diode equation
    or to the source file ``diode.py`` file for the other parameters.

    """
    def __init__(self, name, IS=None, N=None, NBV=None, ISR=None, NR=None, RS=None,
                 CJ0=None, M=None, VJ=None, FC=None, CP=None, TT=None,
                 BV=None, IBV=None, IKF=None, KF=None, AF=None, FFE=None, TEMP=None,
                 XTI=None, EG=None, TBV=None, TRS=None, TTT1=None, TTT2=None,
                 TM1=None, TM2=None, material=constants.si):
        self.name = name
        self.IS = float(IS) if IS is not None else IS_DEFAULT
        self.N = float(N) if N is not None else N_DEFAULT
        self.NBV = float(NBV) if NBV is not None else NBV_DEFAULT
        self.ISR = float(ISR) if ISR is not None else ISR_DEFAULT
        self.NR = float(NR) if NR is not None else NR_DEFAULT
        self.RS = float(RS) if RS is not None else RS_DEFAULT
        self.CJ0 = float(CJ0) if CJ0 is not None else CJ0_DEFAULT
        self.M = float(M) if M is not None else M_DEFAULT
        self.VJ = float(VJ) if VJ is not None else VJ_DEFAULT
        self.FC = float(FC) if FC is not None else FC_DEFAULT
        self.CP = float(CP) if CP is not None else CP_DEFAULT
        self.TT = float(TT) if TT is not None else TT_DEFAULT
        self.BV = float(BV) if BV is not None else BV_DEFAULT
        self.IBV = float(IBV) if IBV is not None else IBV_DEFAULT
        self.IKF = float(IKF) if IKF is not None else IKF_DEFAULT
        self.KF = float(KF) if KF is not None else KF_DEFAULT
        self.AF = float(AF) if AF is not None else AF_DEFAULT
        self.FFE = float(FFE) if FFE is not None else FFE_DEFAULT
        self.TEMP = utilities.Celsius2Kelvin(
            float(TEMP)) if TEMP is not None else TEMP_DEFAULT
        self.XTI = float(XTI) if XTI is not None else XTI_DEFAULT
        self.EG = float(EG) if EG is not None else EG_DEFAULT
        self.TBV = float(TBV) if TBV is not None else TBV_DEFAULT
        self.TRS = float(TRS) if TRS is not None else TRS_DEFAULT
        self.TTT1 = float(TTT1) if TTT1 is not None else TTT1_DEFAULT
        self.TTT2 = float(TTT2) if TTT2 is not None else TTT2_DEFAULT
        self.TM1 = float(TM1) if TM1 is not None else TM1_DEFAULT
        self.TM2 = float(TM2) if TM2 is not None else TM2_DEFAULT
        self.T = T_DEFAULT
        self.last_vd = None
        self.VT = constants.Vth(self.T)
        self.material=material

    def print_model(self):
        strm = ".model diode %s IS=%g N=%g ISR=%g NR=%g RS=%g CJ0=%g M=%g " + \
               "VJ=%g FC=%g CP=%g TT=%g BV=%g IBV=%g KF=%g AF=%g FFE=%g " + \
               "TEMP=%g XTI=%g EG=%g TBV=%g TRS=%g TTT1=%g TTT2=%g TM1=%g " + \
               "TM2=%g"
        print(strm % (self.name, self.IS, self.N, self.ISR, self.NR, self.RS,
                      self.CJ0, self.M, self.VJ, self.FC, self.CP, self.TT,
                      self.BV, self.IBV, self.KF, self.AF, self.FFE, self.TEMP,
                      self.XTI, self.EG, self.TBV, self.TRS, self.TTT1,
                      self.TTT2, self. TM1, self. TM2))


    @utilities.memoize
    def get_i(self, vext, dev):
        if dev.T != self.T:
            self.set_temperature(dev.T)
        if not self.RS:
            i = self._get_i(vext) * dev.AREA
            dev.last_vd = vext
        else:
            vd = dev.last_vd if dev.last_vd is not None else 10*self.VT
            vd = newton(self._obj_irs, vd, fprime=self._obj_irs_prime,
                        args=(vext, dev), tol=options.vea, maxiter=500)
            i = self._get_i(vext-vd)
            dev.last_vd = vd
        return i


    def _obj_irs(self, x, vext, dev):
        # obj fn for newton
        return x/self.RS-self._get_i(vext-x)*dev.AREA

    def _obj_irs_prime(self, x, vext, dev):
        # obj fn derivative for newton
        # first term
        ret = 1./self.RS
        # disable RS
        RSSAVE = self.RS
        self.RS = 0
        # second term
        ret += self.get_gm(self, 0, (vext-x,), 0, dev)
        # renable RS
        self.RS = RSSAVE
        return ret

    def _safe_exp(self, x):
        return np.exp(x) if x < 70 else np.exp(70) + 10 * x

    def _get_i(self, v):
        i_fwd= self.IS * (self._safe_exp(v/(self.N * self.VT)) - 1)
        i_rec= self.ISR* (self._safe_exp(v/(self.NR * self.VT)) - 1)
        i_rev=-self.IS * (self._safe_exp(-(v+self.BV)/(self.NBV *self.VT)) - 1)
        k_inj = 1
        if (not isinf(self.IKF)) and (self.IKF>0) and (i_fwd>0):
            k_inj = sqrt(self.IKF/(self.IKF+i_fwd))
        
        return k_inj*i_fwd+i_rec+i_rev

    @utilities.memoize
    def get_gm(self, op_index, ports_v, port_index, dev):
        if dev.T != self.T:
            self.set_temperature(dev.T)
        v=ports_v[0]
        gm = self.IS / (self.N * self.VT) *\
            self._safe_exp(v / (self.N * self.VT)) +\
            -self.IS/self.VT * (self._safe_exp(-(v+self.BV)/self.VT)) +\
            self.ISR / (self.NR * self.VT) *\
            self._safe_exp(v / (self.NR * self.VT))
        
        if self.RS != 0.0:
            gm = 1. / (self.RS + 1. / (gm + 1e-3*options.gmin))
        return dev.AREA * gm


    def __str__(self):
        pass

    def set_temperature(self, T):
        T = float(T)
        self.EG = self.material.Eg(T) if self.material!=None else self.EG
        self.IS = self.IS*(T/self.T)**(self.XTI/self.N)* \
                  np.exp(-constants.e*(self.material.Eg(constants.Tref) if self.material!=None else self.EG)/\
                         (self.N*constants.k*T)*
                         (1 - T/self.T))
        self.BV = self.BV - self.TBV*(T - self.T)
        self.RS = self.RS*(1 + self.TRS*(T - self.T))
        self.T = T